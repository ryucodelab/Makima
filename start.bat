@echo off
TITLE Zero Two bot
:: Enables virtual env mode and then starts zerotwo
env\scripts\activate.bat && py -m tg_bot
