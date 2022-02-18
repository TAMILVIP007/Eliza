from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot
from userbot.events import register


@register(outgoing=True, pattern="^.fastboot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = 'fastboot'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{fboot} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.adb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    adb = 'adb'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{adb} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.afh(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    afh = 'afh'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{afh} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.aex(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    aex = 'aex'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{aex} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.aosip(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    aosip = 'aosip'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{aosip} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.reapk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    reapk = 'reapk'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{reapk} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.am(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    am = 'am'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{am} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.aqua(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    aqua = 'aqua'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{aqua} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.arrow(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    arrow = 'arrow'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{arrow} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.aicp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    aicp = 'aicp'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{aicp} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.asus(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    asus = 'asus'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{asus} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.bootleg(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    bootleg = 'bootleg'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{bootleg} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.caf(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    caf = 'caf'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{caf} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.candy(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    candy = 'candy'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{candy} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.carbon(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    carbon = 'carbon'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{carbon} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.top(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    top = 'top'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{top} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.popular(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    popular = 'popular'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{popular} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.apk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    apk = 'apk'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{apk} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.discover(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    discover = 'discover'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{discover} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.colt(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    colt = 'colt'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{colt} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.cosp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    cosp = 'cosp'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{cosp} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.crdroid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    crdroid = 'crdroid'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{crdroid} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.ddump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ddump = 'ddump'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{ddump} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.ddog(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ddog = 'ddog'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{ddog} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.dev(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    dev = 'dev'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{dev} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.astudio(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    astudio = 'astudio'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{astudio} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.cs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    cs = 'cs'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{cs} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")

            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.deviceinfos(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    deviceinfos = 'deviceinfos'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{deviceinfos} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.codename(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    codename = 'codename'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{codename} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.specs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = 'specs'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{specs} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.dotos(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    dotos = 'dotos'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{dotos} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.du(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    du = 'du'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{du} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.dump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    dump = 'dump'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{dump} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.evox(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    evox = 'evox'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{evox} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.fdroid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fdroid = 'fdroid'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{fdroid} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.gapps(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    gapps = 'gapps'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{gapps} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.gcam(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    gcam = 'gcam'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{gcam} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.repos(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    repos = 'repos'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{repos} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.commits(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    commits = 'commits'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{commits} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.getdump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    getdump = 'getdump'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{getdump} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.ps(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ps = 'ps'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{ps} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.gsi(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    gsi = 'gsi'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{gsi} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.havoc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    havoc = 'havoc'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{havoc} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.huawei(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    huawei = 'huawei'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{huawei} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.kraken(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    kraken = 'kraken'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{kraken} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.labs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    labs = 'labs'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{labs} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.licrog(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    licrog = 'licrog'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{licrog} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.lineage(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    lineage = 'lineage'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{lineage} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.magisk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    magisk = 'magisk'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{magisk} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.microg(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    microg = 'microg'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{microg} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.moto(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    moto = 'moto'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{moto} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.nanodroid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    nanodroid = 'nanodroid'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{nanodroid} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.omni(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    omni = 'omni'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{omni} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.op(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    op = 'op'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{op} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.oppo(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    oppo = 'oppo'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{oppo} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.of(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    of = 'of'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{of} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.pe(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pe = 'pe'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{pe} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.pdust(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pdust = 'pdust'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{pdust} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.pixy(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pixy = 'pixy'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{pixy} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.potato(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    potato = 'potato'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{potato} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.realme(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    realme = 'realme'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{realme} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.revenge(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    revenge = 'revenge'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{revenge} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.rr(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    rr = 'rr'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{rr} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.samdump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    samdump = 'samdump'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{samdump} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.sonydump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    sonydump = 'sonydump'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{sonydump} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.superior(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    superior = 'superior'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{superior} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.syberia(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    syberia = 'syberia'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{syberia} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.twrp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    twrp = 'twrp'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{twrp} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.viper(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    viper = 'viper'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{viper} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.devdb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    devdb = 'devdb'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{devdb} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.xiaomi(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    xiaomi = 'xiaomi'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{xiaomi} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.xposed(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    xposed = 'xposed'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{xposed} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.xtended(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    xtended = 'xtended'
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=995271804)
            )
            await conv.send_message(f"/{xtended} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @android_helper_bot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
