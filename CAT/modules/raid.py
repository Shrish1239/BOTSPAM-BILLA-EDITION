import asyncio

from random import choice

from telethon import events

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from CAT.data import RAID, CAT_LOVER, MRAID, SRAID, CRAID, CAT_LOVER

REPLY_RAID = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in CAT_LOVER:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ.")
            elif uid == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif uid in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"{hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(RAID)),
            reply_to=event.message.id,
        )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in CAT_LOVER:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ.")
            elif user_id == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif user_id in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» BILLA ENKI MA CHODEGA AB !! ✅")
        except NameError:
            await e.reply(f"» {hl}rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» BETA TUZE MAFF KIYA JA !! ✅")
        except NameError:
            await e.reply(f"{hl}drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def mraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"{hl}mraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def sraid(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"{hl}sraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def craid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in CAT_LOVER:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ.")
            elif uid == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif uid in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(CRAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"» {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)
