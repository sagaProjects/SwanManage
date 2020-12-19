from wbb import app
from pyrogram import filters, emoji
import asyncio


MESSAGE = "{} Welcome {}!"


@app.on_message(filters.new_chat_members)
async def welcome(client, message):
    new_members = [i.mention for i in message.new_chat_members]
    text = MESSAGE.format(emoji.CROWN, ",  ".join(new_members))
    m = await message.reply_text(text, disable_web_page_preview=True)
    await asyncio.sleep(20)
    await m.delete()