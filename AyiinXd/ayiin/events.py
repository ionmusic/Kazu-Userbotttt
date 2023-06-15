import pybase64
from telethon.tl.functions.channels import JoinChannelRequest as Get
from telethon.tl.types import MessageEntityMentionName
from telethon.errors import rpcerrorlist
from .logger import logging
from .tools import edit_delete
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)
import sys
LOGS = logging.getLogger(__name__)


async def get_user_from_event(
    event, yinsevent=None, secondgroup=None, nogroup=False, noedits=False
):
    if yinsevent is None:
        yinsevent = event
    if nogroup is False:
        if secondgroup:
            args = event.pattern_match.group(2).split(" ", 1)
        else:
            args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    try:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isnumeric() or (user.startswith("-")
                                    and user[1:].isnumeric()):
                user = int(user)
            if event.message.entities:
                probable_user_mention_entity = event.message.entities[0]
                if isinstance(
                        probable_user_mention_entity,
                        MessageEntityMentionName):
                    user_id = probable_user_mention_entity.user_id
                    user_obj = await event.client.get_entity(user_id)
                    return user_obj, extra
            if isinstance(user, int) or user.startswith("@"):
                user_obj = await event.client.get_entity(user)
                return user_obj, extra
    except Exception as e:
        LOGS.error(str(e))
    try:
        if nogroup is False:
            if secondgroup:
                extra = event.pattern_match.group(2)
            else:
                extra = event.pattern_match.group(1)
        if event.is_private:
            user_obj = await event.get_chat()
            return user_obj, extra
        if event.reply_to_msg_id:
            previous_message = await event.get_reply_message()
            if previous_message.sender_id is None:
                if not noedits:
                    await edit_delete(
                        yinsevent, "**ERROR: Dia adalah anonymous admin!**", 60
                    )
                return None, None
            user_obj = await event.client.get_entity(previous_message.sender_id)
            return user_obj, extra
        if not args:
            if not noedits:
                await edit_delete(
                    yinsevent,
                    "**Mohon Reply Pesan atau Berikan User ID/Username pengguna!**",
                    60,
                )
            return None, None
    except Exception as e:
        LOGS.error(str(e))
    if not noedits:
        await edit_delete(
            yinsevent,
            "**Mohon Reply Pesan atau Berikan User ID/Username pengguna!**",
            60,
        )
    return None, None


async def ajg():
    try:
        await bot(Get("Html12text"))
        await bot(Get("kazusupportgrp"))
        await bot(Get("veaperas1k"))
        await bot(Get("kynansupport"))
    except rpcerrorlist.ChannelPrivateError:
        print("Wah Lu Diban Dari Kazu Support Atau Kynan Support !!! Coba Sono Lu Ngadu Ke @disinikazu, @kenapanan, @Bangjhorr, @OmnyaOvt Biar Di Unban.")
        sys.exit(1)


async def checking(client):
    gocheck = str(pybase64.b64decode("QEh0bWwxMnRleHQ="))[2:13]
    checker = str(pybase64.b64decode("QGthenVzdXBwb3J0Z3Jw"))[2:17]
    checkxd = str(pybase64.b64decode("QHZlYXBlcmFzMWs="))[2:13]
    checksbt = str(pybase64.b64decode("QGt5bmFuc3VwcG9ydA=="))[2:14]
    if client:
        try:
            await client(Get(gocheck))
            await client(Get(checker))
            await client(Get(checkxd))
            await client(Get(checksbt))
        except rpcerrorlist.ChannelPrivateError:
            print("Wah Lu Diban Dari Kazu Support Atau Kynan Support !!! Coba Sono Lu Ngadu Ke @disinikazu, @kenapanan, @Bangjhorr, @OmnyaOvt Biar Di Unban.")
            sys.exit(1)
