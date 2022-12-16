from asyncio import sleep
from pyrogram import filters
from wbb import app
from wbb.core.decorators.permissions import adminsOnly

__MODULE__ = "Tagall"
__HELP__ = """/all - mention all members
/cancel - stop mention
"""

spam_chats = []

@app.on_message(filters.command("tagall") & filters.group)
@adminsOnly("Minimal_Ijin_Tod")
async def mentionall(client, message):
    await message.delete()
    chat_id = message.chat.id
    tai = message.reply_to_message
    ppk = message.text.split(None, 1)[1]
    if not tai and not ppk:
        return await message.reply("__Tolong berikan saya pesan atau balas ke pesan__")
   

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ''
    async for usr in app.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 5:
            if ppk:
                txt = f"{ppk}\n{usrtxt}"
                await app.send_message(chat_id, txt)
            elif tai:
                await tai.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ''
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command("cancel") & filters.group)
@adminsOnly("can_delete_messages")
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("__Sepertinya tidak ada tagall disini...__")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("__Udah Ya Tod Jangan Spam.__")
