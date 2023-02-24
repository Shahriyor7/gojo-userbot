from telethon import TelegramClient, events, sync

@events.register(events.NewMessage(pattern=".me"))
async def test(event):
	await event.edit("@SHAHRIYORBEK1")
	
