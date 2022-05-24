from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from telethon import events
import os
import random
import sys


@Riz.on(events.NewMessage(pattern=".x"))
@Riz2.on(events.NewMessage(pattern=".x"))
@Riz3.on(events.NewMessage(pattern=".x"))
@Riz4.on(events.NewMessage(pattern=".x"))
@Riz5.on(events.NewMessage(pattern=".x"))
@Riz6.on(events.NewMessage(pattern=".x"))
@Riz7.on(events.NewMessage(pattern=".x"))
@Riz8.on(events.NewMessage(pattern=".x"))
@Riz9.on(events.NewMessage(pattern=".x"))
@Riz10.on(events.NewMessage(pattern=".x"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "Rebooting......!!\n\n[][][][][][][][][][][][][][][][][][][][][]\n\nBaby 🥺✨❤️\nJust wait for the few minutes.\n\n[][][][][][][][][][][][][][][][][][][][][]\n\n⚙ Server :\n@M8N_OFFICIAL"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Riz.disconnect()
        except Exception:
            pass
        try:
            await Riz2.disconnect()
        except Exception:
            pass
        try:
            await Riz3.disconnect()
        except Exception:
            pass
        try:
            await Riz4.disconnect()
        except Exception:
            pass
        try:
            await Riz5.disconnect()
        except Exception:
            pass
        try:
            await Riz6.disconnect()
        except Exception:
            pass
        try:
            await Riz7.disconnect()
        except Exception:
            pass
        try:
            await Riz8.disconnect()
        except Exception:
            pass
        try:
            await Riz9.disconnect()
        except Exception:
            pass
        try:
            await Riz10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
