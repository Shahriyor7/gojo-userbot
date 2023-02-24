from telethon import TelegramClient, events, sync, functions, types, Button

import zeus.client
client = zeus.client.client
@events.register(events.NewMessage(outgoing=True, pattern=".help"))
async def help(event):
	await event.edit("""
🛠 Umumiy modullar: 61
⚒ Berkitilgan modullar:  0

GOJO-USERBOT HELP MENU
[01] Bombs - Animation emojise — .bombs
[02] Help - Help menu — .help
[03] Loading  - Animation loading — .loading
[04] Emoji  -  Emoji text editor - .emoji <here text>
[05] Dump - Candy dump animate - .dump
[06] Typer - Animation write text - .type <here text>
[07] Lul - animatsia lul - .lul
[08] Snake - Snake animation - .snake 
[19] Nothappy - Abimation Nothappy - .nothappy
[10] Clock - animation clock - .clock
[11] Muah - animation - .muah
[12] Heart - animation - .heart
[13] Gym - animation gymnastic - .gym
[14] Earth - animation globus - .earth
[15] Moon - animation - .moon
[16] Candy - Animatiln - .candy
[17] Smoon - animation - .smoon
[18] Tmoon - animation - .tmoon
[19] Clown - animation - .clown
[20] Star - batterfly and star animation - .star
[21] Boxs - Color animation - .boxs
[22] Rain - water animation - .rain
[23] Clol - "What?" snimation - .clol
[24] Odra - Animation - .odra 
[25] Fleaveme - animation - .fleaveme
[26] Loveu - love animation - .loveu
[27] Plane - animation - .plane
[28] Police - animation sirena - .police
[29] Solarsystem - animation - .solarsystem
[30] Chatinfo - function scan chatinfo - .chatinfo  
[31] M.Q - Memocyte Quote - .mq <reply text>
[32] Mute - Admin function - .mute (m, h, d )
[33] N.Q - Nedo Quote - .nq <reply text>
[34] Fuck - Fuck you - .fuck
[35] Rev - reverse - .rev
[36] Tr - Translator - .tr <language code > <reply message>
[37] Userinfo - Username information - .userinfo <reply>
[38] Base64 - encode and decode  text messages - .b64 en <reply text> .b64 de <reply encoded message>
[39] React - reactions - .react help
[40] Snow - animation snow - .snow
[41] Tts - text to voice - .tts <lang code> reply text message
[42] Itp - image to pdf - .itp reply to image
[43] About clock - datetime - .aboutclock <number>
[44] clocku - firstname clock - .clocku <number> <nickname>
[45] timer - timer animation - .timer <number>
[46] Afk - Afk mode - .afkon <text> / .afkoff / .afkstatus
[47] numbers - Numbers - .numbers <number>
[48] tag all - tag group members - .tagall
[49] magic - animation hearts - .magic
[50] sda - find delete accounts - .sda
[51] drc - o'chib ketuvchi rasmni saqlash' - .rcd
[52] rda - remove delete accounts - .rda
[53] ip trace - ip osint - .iptrace <ip addres>
[54] rename - Rename firstname and last name - .rename <nick> // <first name>
[55] Alive - information gojo userbot - .alive
[56] Qr code - qr code creator - .qrc create <reply>
[57] Sms flood - Spam message  - .spam <time> <count> <text>
[68] rts - save  message - .rts
[59] rgm - reload get message - rgm
	""")
