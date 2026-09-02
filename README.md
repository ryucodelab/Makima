<p align="center">
  <img src="https://github.com/ryucodelab/Zero-Two/blob/787fa910ace276007c17fccfa9ee70ee06b6cfe1/images.jpeg" alt="Zero Two Banner" width="100%">
</p>

<h1 align="center">Zero Two (ゼロツー)</h1>

<p align="center">
  A powerful, modular, anime-themed Telegram group management bot with anti-raid & sybil detection.
</p>

<p align="center">
  <a href="https://t.me/Codename002_bot"><img src="https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram&style=for-the-badge" alt="Telegram Bot"></a>
  <a href="https://t.me/pbshinigami"><img src="https://img.shields.io/badge/Support-Group-2CA5E0?logo=telegram&style=for-the-badge" alt="Support Group"></a>
  <a href="https://github.com/ryucodelab/Zero-Two/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-GPLv3-green?style=for-the-badge" alt="License"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-yellow?logo=python&style=for-the-badge" alt="Python Version">
  <img src="https://img.shields.io/badge/Maintained-Yes-brightgreen?style=for-the-badge" alt="Maintained">
</p>

---

## 📖 About

**Zero Two** is a feature-rich Telegram group management bot built for communities that need reliable moderation tools, anti-raid protection, and a sybil-resistant defense system — wrapped in a clean, anime-inspired identity.

Try the live bot here → **[@Codename002_bot](https://t.me/Codename002_bot)**

---

## ✨ Features

- 🛡️ Anti-raid & sybil detection system
- 👮 Full group management & moderation toolkit
- 🔨 Ban / mute / warn systems with logging
- 🌐 Federation (Fed) ban support
- 🧩 Modular, extensible codebase
- ⚙️ Highly configurable via `config.ini`

---

## 🚀 How to Setup

```bash
git clone https://github.com/ryucodelab/Zero-Two
cd Zero-Two
cp sample_config.ini config.ini
```

Fill in all the required variables in `config.ini` (see the [Configuration](#-configuration) section below), then:

```bash
pip3 install -U -r requirements.txt
python3 -m tg_bot
```

---

## ⚙️ Configuration

Edit your `config.ini` file with the following variables:

| Variable | Description | Where to get it |
|---|---|---|
| `log` | Enable/disable logging | `True` / `False` |
| `APP_ID` | Telegram App ID | [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Telegram API Hash | [my.telegram.org](https://my.telegram.org) |
| `TOKEN` | Your bot token | [@BotFather](https://t.me/BotFather) |
| `OWNER_ID` | Your Telegram user ID | — |
| `OWNER_USERNAME` | Your Telegram username | — |
| `SQLALCHEMY_DATABASE_URI` | PostgreSQL database URL | Your DB provider |
| `MESSAGE_DUMP` | Log group/channel ID | — |
| `GBAN_LOGS` | Gban log group/channel ID | — |
| `SYS_ADMIN` | Sudo/system admin user IDs | — |
| `LOAD` | Modules to load (whitelist) | — |
| `NO_LOAD` | Modules to skip loading | e.g. `sed` |
| `WEBHOOK` | Enable webhook mode | `True` / `False` |
| `SPB_MODE` | Single process bot mode | `True` / `False` |
| `URL` | Webhook URL | — |
| `INFOPIC` | Show profile picture on info command | `True` / `False` |
| `CERT_PATH` | SSL certificate path | — |
| `PORT` | Webhook port | e.g. `5000` |
| `DEL_CMDS` | Auto-delete command messages | `True` / `False` |
| `STRICT_GBAN` | Strict global ban enforcement | `True` / `False` |
| `BAN_STICKER` | Custom sticker on ban | — |
| `ALLOW_EXCL` | Allow `!` as command prefix | `True` / `False` |
| `CUSTOM_CMD` | Enable custom command prefix | `True` / `False` |
| `CASH_API_KEY` | Currency/stock API key | [AlphaVantage](https://www.alphavantage.co/support/#api-key) |
| `TIME_API_KEY` | Timezone API key | [TimezoneDB](https://timezonedb.com/api) |
| `WALL_API` | Wallpaper API key | [Alpha Coders](https://wall.alphacoders.com/api.php) |
| `spamwatch_api` | SpamWatch API token | [@SpamWatchBot](https://t.me/SpamWatchBot) |
| `SPAMMERS` | Manual spammer ID list | — |
| `LASTFM_API_KEY` | Last.fm API key | [Last.fm API](https://www.last.fm/api/account/create) |
| `BOT_API_URL` | Telegram Bot API base URL | `https://api.telegram.org/bot` |
| `BOT_API_FILE_URL` | Telegram Bot API file URL | `https://api.telegram.org/file/bot` |
| `REDIS_URI` | Full Redis connection string (takes priority over the fields below) | Your Redis provider, e.g. `rediss://default:password@host:6379/0` |
| `REDIS_HOST` | Redis host (used only if `REDIS_URI` is not set) | Default: `localhost` |
| `REDIS_PORT` | Redis port (used only if `REDIS_URI` is not set) | Default: `6379` |
| `REDIS_DB` | Redis database index (used only if `REDIS_URI` is not set) | Default: `0` |
| `REDIS_PASSWORD` | Redis password (used only if `REDIS_URI` is not set) | — |

> 💡 Leave a variable blank only if the module using it is not required for your deployment.

> ⚙️ **Redis setup:** if you're using a hosted Redis provider (Upstash, Redis Cloud, Railway, etc.), just set `REDIS_URI` to the full connection string they give you — it's the easiest option and takes priority over the individual `REDIS_HOST`/`PORT`/`DB`/`PASSWORD` fields. Only fill in those separate fields if you're running Redis yourself without a single connection URI. Leaving both unset makes the bot fall back to `localhost:6379`.

---

## 💬 Support & Questions

Got issues, questions, or want to hang out with the community?

👉 Join our support group: **[@pbshinigami](https://t.me/pbshinigami)**

---

## 🙏 Credits

This project stands on the shoulders of the developers who built and maintained the codebase this bot is forked from:

- **[Marie](https://github.com/PaulSonOfLars/tgbot)** — Original bot framework
- **[Rose](https://github.com/Marie-and-friends/Rose)** — Core feature contributions
- **[Paul Larsen (PaulSonOfLars)](https://github.com/PaulSonOfLars)** — Creator of the original Marie/Rose codebase

Without their foundational work, this project would not exist. All credit for the core architecture goes to the original authors and contributors.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/ryucodelab">ryucodelab</a> — part of the <b>Blue Blood Union</b> ecosystem
</p>
