from ubot import *

__MODULE__ = "Pinterest"
__HELP__ = """
 Bantuan Untuk Pinterest


• Perintah: <code>{0}pinter</code> [link]
• Penjelasan: Untuk mengunduh media dari pinterest.
"""


@PY.UBOT("pinter")
async def _(client, message):
    await pinterit(client, message)