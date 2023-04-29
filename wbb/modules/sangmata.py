import asyncio

from pyrogram import filters

from wbb import app, app2

__MODULE__ = "SangMata"
__HELP__ = """/sg - Balas ke pengguna atau username atau id"""

@app.on_message(filters.command("sg"))
async def sangmata(client, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        anu = message.text.split(None, 1)[1]
        iya = await app.get_users(anu)
        user = iya.id
    else:
        return await message.reply(
            "__Balas ke pesan orang atau ketik username/id orang__"
        )
    user_id = user
    sgbot = await message.reply("**🔍 Lu Siapa Sih Tod**")
    await app2.unblock_user("@sangmata_beta_bot")
    sang = await app2.send_message("SangMata_beta_bot", f" {user_id}")
    await sang.delete()
    await asyncio.sleep(3)
    async for msg in app2.search_messages("SangMata_beta_bot", limit=4):
        if "This result is incomplete" or "Link To Profile" in msg.text:
            await msg.delete()
        if "No records found" in msg.text:
            await sgbot.edit("Tidak ada catatan tentang user ini")
            await msg.delete()
        if "Name" in msg.text:
            await sgbot.edit(msg.text)
            await msg.delete()
            
