""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("command"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Commands For ravana69/UniBorg:**\n\n`.info`\n`.pname`\n`.ppic`\n`.pbio`\n`.afk text`\n`.afk`\n`.alive`\n`.baalaji`\n`.admin`\n`.admem\n.sclock\n.cname\n.coin\n.scd text\n.cd text\n.fadmin\n.create b\n.create g\n.create c\n.currency usd inr\n.eye\n.z\n.lslocal\n.savefilter\n.listfilters\n.clearfilter\n.fu\n.kess\n.sux\n.gaali\n.drive\n.get_admin\n.get_bot\n`.get_id`\n`.github`\n`.commit`\n`.leave`\n`.loda`\n`.meme`\n`.🖕`\n`.smoon`\n`.tmoon`\n`.music`\n.ocr\n.weather\n.paste\n.approvepm\n.blockpm\n.listapprovedpms\n.restart\n.reboot\n.fastboot\n.shutdown\n.purge\n.quickheal\n.vqh\n.vquickheal\n.remove.bg\n.sca\n.screencapture\ns/old text/new text\n.shout text\n.spem\n.slap\n.snips\n.snipd\n.snipl\n.solar\n.speedtest image/text\n.stat\n.kangsticker\n.tr language code\n.tts language code\n.telegraph text/media\n.time\n.z\n.repo\n.download\n.upload\n.verystream\n.warn(1-3)\n.gbun\n.savewelcome\n.clearwelcome\n.whois\n.wiki\n.starttor\n.addmag\n.addtor\n.addurl\n.ariaRM\n.ariaP\n.ariaResume\n.showariastatus\n.bar\n.chu\n.dns\n.url\n.unshort\n.myip\n.myisp\n.mywho\n.myup\n.myhead\n.decide\n.join\n.pay\n.direct gdrive/mega etc\n.uptime\n.cpu\n.suicide\n.stdplugins\n.pip\n.date\n.env\n.neofetch\n.fsave\n.ftrim\n.floodwarn\n.gey\n.abuse\n.pro\n.insult\n.rape\n.metoo\n.runs\n.dsearch\n.ddir\n.gfolder\n.gdl\n.glink\n.gs text 2 search **I Don't Use Any Other Plugins Other Than These ,So Haven't Included Others Here...**"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
