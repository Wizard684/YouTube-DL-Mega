
from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url But You must join my Updation channel👉👉 @Mega_Bots_Updates"
    await message.reply_text(helptxt)
