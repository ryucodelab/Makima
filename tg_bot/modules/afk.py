import html
import random
import datetime

from telegram import Update, MessageEntity
from telegram.ext import Filters, CallbackContext
from telegram.error import BadRequest
from tg_bot.modules.sql import afk_sql as sql
from tg_bot.modules.users import get_user_id
from tg_bot.modules.helper_funcs.decorators import kigcmd, kigmsg, rate_limit


def time_ago(dt: datetime.datetime) -> str:
    """Humanize a datetime into a '... ago' string."""
    if not dt:
        return "Unknown"

    now = datetime.datetime.utcnow()
    seconds = int((now - dt).total_seconds())
    if seconds < 0:
        seconds = 0

    if seconds < 60:
        return f"{seconds} second{'s' if seconds != 1 else ''} ago"

    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"

    hours = minutes // 60
    if hours < 24:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"

    days = hours // 24
    if days < 30:
        return f"{days} day{'s' if days != 1 else ''} ago"

    months = days // 30
    if months < 12:
        return f"{months} month{'s' if months != 1 else ''} ago"

    years = months // 12
    return f"{years} year{'s' if years != 1 else ''} ago"


@kigmsg(Filters.regex("(?i)^brb"), friendly="afk", group=3)
@kigcmd(command="afk", group=3)
@rate_limit(40, 60)
def afk(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    user = update.effective_user
    chat = update.effective_chat

    if not user:  # ignore channels
        return

    if user.id in (777000, 1087968824):
        return

    notice = ""
    if len(args) >= 2:
        reason = args[1]
        if len(reason) > 100:
            reason = reason[:100]
            notice = "\nYour afk reason was shortened to 100 characters."
    else:
        reason = ""

    sql.set_afk(user.id, chat.id, reason)
    fname = user.first_name
    try:
        update.effective_message.reply_text("{} is now away!{}".format(fname, notice))
    except BadRequest:
        pass


@kigmsg(
    (
        Filters.all
        & Filters.chat_type.groups
        & ~Filters.user(777000)
        & ~Filters.command(["afk"])
        & ~Filters.regex("(?i)^brb")
    ),
    friendly='afk',
    group=1,
)
@rate_limit(40, 60)
def no_longer_afk(update: Update, context: CallbackContext):
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message

    if not user:  # ignore channels
        return

    afk_d = sql.check_afk_status(user.id, chat.id)
    was_afk = bool(afk_d and afk_d.is_afk)
    reason = afk_d.reason if afk_d else ""
    since_text = time_ago(afk_d.time) if afk_d else ""

    res = sql.rm_afk(user.id, chat.id)
    if res and was_afk:
        if message.new_chat_members:  # dont say msg
            return
        firstname = user.first_name
        try:
            options = [
                "{} is here!",
                "{} is back!",
                "{} is now in the chat!",
                "{} is awake!",
                "{} is back online!",
                "{} is finally here!",
                "Welcome back! {}",
                "Where is {}?\nIn the chat!",
            ]
            chosen_option = random.choice(options)
            welcome_text = chosen_option.format(html.escape(firstname))

            extra_lines = []
            if reason:
                extra_lines.append(
                    f"• Reason: <code>{html.escape(reason)}</code>"
                )
            extra_lines.append(f"🕐 Since: <code>{since_text}</code>")

            full_text = welcome_text + "\n\n" + "\n".join(extra_lines)

            update.effective_message.reply_text(full_text, parse_mode="html")
        except Exception:
            return


@kigmsg(
    (
        Filters.reply
        | Filters.entity(MessageEntity.MENTION)
        | Filters.entity(MessageEntity.TEXT_MENTION)
    )
    & Filters.chat_type.groups,
    friendly='afk',
    group=8,
)
@rate_limit(40, 60)
def reply_afk(update: Update, context: CallbackContext):
    bot = context.bot
    message = update.effective_message
    userc = update.effective_user
    chat = update.effective_chat
    if not userc:
        return
    userc_id = userc.id
    if message.entities and message.parse_entities(
        [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]
    ):
        entities = message.parse_entities(
            [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]
        )

        chk_users = []
        for ent in entities:
            if ent.type == MessageEntity.TEXT_MENTION:
                user_id = ent.user.id
                fst_name = ent.user.first_name

            elif ent.type == MessageEntity.MENTION:
                user_id = get_user_id(
                    message.text[ent.offset : ent.offset + ent.length]
                )
                if not user_id:
                    # Should never happen, since for a user to become AFK they must have spoken. Maybe changed username?
                    continue

                try:
                    fetched_chat = bot.get_chat(user_id)
                except BadRequest:
                    print(f"Error: Could not fetch user id {user_id} for AFK module")
                    continue
                fst_name = fetched_chat.first_name

            else:
                continue

            if user_id in chk_users:
                continue
            chk_users.append(user_id)

            check_afk(update, context, user_id, fst_name, userc_id, chat.id)

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        fst_name = message.reply_to_message.from_user.first_name
        check_afk(update, context, user_id, fst_name, userc_id, chat.id)


def check_afk(update, context, user_id, fst_name, userc_id, chat_id):
    if int(userc_id) == int(user_id):
        return
    afk_d = sql.check_afk_status(user_id, chat_id)
    if not afk_d:
        return
    is_afk = afk_d.is_afk
    if is_afk:
        since_text = time_ago(afk_d.time)
        if reason := afk_d.reason:
            res = (
                f"{html.escape(fst_name)} is afk.\n\n"
                f"• Reason: <code>{html.escape(reason)}</code>\n"
                f"🕐 Since: <code>{since_text}</code>"
            )
        else:
            res = (
                f"{html.escape(fst_name)} is afk.\n\n"
                f"🕐 Since: <code>{since_text}</code>"
            )
        update.effective_message.reply_text(res, parse_mode="html")


def __gdpr__(user_id):
    sql.rm_afk_all(user_id)


from tg_bot.modules.language import gs

def get_help(chat):
    return gs(chat, "afk_help")

__mod_name__ = "AFK"
