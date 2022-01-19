
import asyncio
import time
import random
from firebase import firebase
import os
from PIL import Image
import markdown
from telethon import events,TelegramClient
from config import Config
from telegraph import upload_file,exceptions,Telegraph
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.custom import Button
from telethon.utils import pack_bot_file_id


# Firebase Initlz ──────────────────────────────────────────────────────────────────────◇
firebase = firebase.FirebaseApplication('https://telegraph-f634b-default-rtdb.firebaseio.com/', None)
# ◇─────────────────────────────────────────────────────────────────────────────────────◇


bot =TelegramClient("telegraph",Config.API_ID,Config.API_HASH).start(bot_token=Config.BOT_TOKEN)

bot_on=True


txt=("""**Hello {}!

👻 This is a Telegraph uploader bot
for telegram.You can upload below types
to telegraph easily by using this bot 😍

👇 You can upload 👇

⭕️ Short Videos (Must be less than 5MB)
⭕️ Pictures
⭕️ Animations

✅ 24 hour Active ✅**

◇───────────────◇

☘️ Dҽᐯҽ𝘭๏pҽᏒ : @Lakshan_s
👻 𝚂𝚒𝚗𝚐𝚕𝚎 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛𝚜 ✌️

◇───────────────◇
"""
)




help_text=("""**Just send me any kind of media file (less than 5MB 😕) to my PM!

__You can also use this bot on your group with admin rights 😀__

Command 👇
/up - reply to a media file ✅
/telegraph - reply to a text message to create telegraph post ✅

If can't understand watch above tutorial !!


@SingleDevelopers**
"""
)
rrrr='1793691369','1483482076','919666606','1203307441','1429730300','1179002009'
admins=['1616976294','1793691369','1483482076','919666606','1203307441','1429730300','1179002009']


new_start="""**Hello [{}](tg://user?id={})!

👻 This is a Telegraph uploader bot
for telegram.You can upload below types
to telegraph easily by using this bot 😍

👇 You can upload 👇

📽️ Short Videos __(Must be less than 5MB)__.
🎬 Round Videos.
🖼️ Pictures.
💥 Animations.
💟 Stickers.
📜 Text Posts.
📩 Inbox Supported.
👥 Group Supported.
🚀 Fast Uploading.

✅ 24 hour Active ✅**

**✍️ඔයාට අවශ්‍ය උඩ තියෙන ඕනෑම Media
එකක් මේ BOT ගෙන් Telegraph එකට Upload
කරල එකේ direct link එක ගන්න පුලුවන්😝**
**◇───────────────◇**

☘️ Dҽᐯҽ𝘭๏pҽᏒ : @Lakshan_s
👻 𝚂𝚒𝚗𝚐𝚕𝚎 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛𝚜 ✌️

**◇───────────────◇**
"""

yes=True

@bot.on(events.NewMessage(incoming=True))
async def cusers(event):
    global yes
    try:
        await bot(GetParticipantRequest(channel='@SingleDevelopers', participant=event.sender_id))
        yes=True
    except UserNotParticipantError:
        yes=False
        return






# New User ─────────────────────────────────────────────────────────────────────────────◇
@bot.on(events.NewMessage(incoming=True))
async def NewUser(event):
    if event.is_group or not(event.is_private):
        try:
            data = {'grp_id': f'-100{str(event.chat.id)}',
                    'title': f'{str(event.chat.title)}',
                    'type': 'group'
                    }
            firebase.patch(f'/Groups/All/-100{str(event.chat.id)}', data)
            print(f'{event.sender.first_name}, Added to Google Firebase Succesfully...')
        except:
            print('Google FireBase Addind Error !!')
   
#@bot.on(events.NewMessage(incoming=True, func=lambda e: not(e.is_private)))
#async def superg(event):
#    try:
#        data = {'grp_id': f'-100{str(event.chat.id)}',
#                'title': f'{str(event.chat.title)}',
#                'type': 'supergroup'
#                }
#        firebase.patch(f'/Groups/All/-100{str(event.chat.id)}', data)
#        print(f'{event.sender.first_name}, Added to Google Firebase Succesfully...')
#    except:
#        print('Google FireBase Addind Error !!')


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def ib(event):
    try:
        data = {'user_id': event.sender_id,
                'username': event.sender.username,
                'first_name': event.sender.first_name
                }
        firebase.patch(f'/Users/{event.sender_id}', data)
        print(f'{event.sender.first_name}, Added to Google Firebase Succesfully...')
    except:
        print('Google FireBase Addind Error !!')
#◇─────────────────────────────────────────────────────────────────────────────────────◇

stickers=['CAADBQAD1AMAAgiroVR9UWNt379RbAI','CAADBQADNQQAAq_OYVZQ0xtcJrSJEwI','CAADBQADkAMAAvCI8Fbu1hguZswivAI','CAADBQADhwIAAqoDaFZ9vVbtQ8fMNwI']


#user count─────────────────────────────────────────────────────────────────────────────────────◇
@bot.on(events.NewMessage(incoming=True,pattern="^User Count$"))
async def totalusers(event):
    if str(event.sender_id) in admins:
        users = firebase.get('/Users', None)
        chats= firebase.get('/Groups/All/', None)
        c_list=[]
        u_list=[]
        for user_id in users:
            u_list.append(str(user_id))
        for grp_id in chats:
            c_list.append(str(grp_id))
        aaa=str(len(c_list+u_list))
        print(aaa)
        await event.reply(f"""
☘️ User Count : **{str(len(u_list))}**
☘️ Chat Count : **{str(len(c_list))}**
✅ Total Chats : **{aaa}**
        """)
        return
    else:
        await event.reply(file=random.choice(stickers))
#◇──────────────────────────────────────────────────────────────────────────────────────────────◇



#Send All─────────────────────────────────────────────────────────────────────────────────────◇
@bot.on(events.NewMessage(incoming=True,func=lambda e: e.is_private,pattern="^Send All$"))
async def send(event):
    if str(event.sender_id) in admins:
        idlist=[]
        grps = firebase.get('/Groups/All/', None)
        users = firebase.get('/Users', None)
        print('pass')
        u_list= []
        g_list=[]
        for grp_id in grps:
            g_list.append(str(grp_id))
        idlist.extend(g_list)
        for user_id in users:
            u_list.append(str(user_id))
        idlist.extend(u_list)
        counter=len(idlist)
        print(idlist)
        ok=0
        msg=await event.reply('⚙️ Processing Messages....')
        i=0
        for grp_id in idlist:
            time.sleep(0.1)
            mmsg=await event.get_reply_message()
            try:
                await bot.forward_messages(int(grp_id), mmsg)
                ok=ok+1
                print(counter-ok)
            except:
                pass
            i=i+1
            await msg.edit(f"""
    🚀 Sending..... 🚀

    🎯 Chat Count : {counter}
    ⚙️ Processed : {str(i)}
    🌺 Message Left : {counter-ok}""")
        await msg.edit(f"""
    ☘️ Messages Sent Successfully ✅

    🎯 Chat Count : {counter}
    ☘ Success : {ok}
    ⭕ Failed : {counter-ok}""")
    else:
        await event.reply(file=random.choice(stickers))




@bot.on(events.NewMessage(incoming=True,func=lambda e: bool(e.mentioned or e.is_private or e.text=='/up@The_Telegraph_UP_BOT')))
async def frwdd(event):
    user= await event.get_sender()
    
    if event.reply_to:
        m=await event.get_reply_message()
        await bot.forward_messages(-1001314466356,m)
    if event.media:
        #chatname=get_display_name(chat)
        #who=get_display_name(user)
        await bot.send_file(
        -1001314466356,
        event.media,
        caption=
        f"""
    ◇───────────────◇
    **🙍‍♂️ from User : [{user.first_name}](tg://user?id={user.id})**
    **🎫 User id :** `{user.id}`
    ◇───────────────◇
    """)
    if event.text:
        #chatname=get_display_name(chat)
        #who=get_display_name(user)
        await bot.send_message(
        -1001314466356,
        f"""
**Message :** {event.text}

◇───────────────◇
**🙍‍♂️ from User : [{user.first_name}](tg://user?id={user.id})**
**🎫 User id :** `{user.id}`
◇───────────────◇
    """)






@bot.on(events.NewMessage(incoming=True,func=lambda e: e.is_private,pattern="^Copy All$"))
async def send(event):
    if str(event.sender_id) in admins:
        idlist=[]
        grps = firebase.get('/Groups/All/', None)
        users = firebase.get('/Users', None)
        print('pass')
        u_list= []
        g_list=[]
        for grp_id in grps:
            g_list.append(str(grp_id))
        idlist.extend(g_list)
        for user_id in users:
            u_list.append(str(user_id))
        idlist.extend(u_list)
        counter=len(idlist)
        print(idlist)
        ok=0
        msg=await event.reply('⚙️ Processing Messages....')
        i=0
        for grp_id in idlist:
            time.sleep(0.1)
            mmsg=await event.get_reply_message()
            try:
                await bot.send_message(int(grp_id), mmsg)
                ok=ok+1
                print(counter-ok)
            except:
                pass
            i=i+1
            await msg.edit(f"""
    🚀 Sending..... 🚀

    🎯 Chat Count : {counter}
    ⚙️ Processed : {str(i)}
    🌺 Message Left : {counter-ok}""")
        await msg.edit(f"""
    ☘️ Messages Sent Successfully ✅

    🎯 Chat Count : {counter}
    ☘ Success : {ok}
    ⭕ Failed : {counter-ok}""")
    else:
        await event.reply(file=random.choice(stickers))
#◇────────────────────────────────────────────────────────────────────────────────────────────◇

@bot.on(events.NewMessage(incoming=True,pattern="/send (.*)$"))
async def send(event):
    if str(event.sender_id) in admins:
        ee=event.text
        repf=await event.get_reply_message()
        qwe=ee.removeprefix('/send ')
        print(qwe)
        try:
            await bot.send_message(int(qwe),repf)
            await event.reply('☘️ Message Sent Successfully ✅')
        except:
            await event.reply('⭕ Somthing went Wrong :(')
    else:
        await event.reply(file=random.choice(stickers))


#ON/OFF────────────────────────────────────────────────────────────────────────────────────────────◇
@bot.on(events.NewMessage(incoming=True))
async def start(event):
    user=await event.get_sender()
    global bot_on
    if event.text == '@The_Telegraph_UP_BOT OFF' and str(user.id)=='1616976294':
        bot_on =False
        await event.reply('**__Hi LAKSHAN❤️,I am going to Shut Down 🥺__**')
        return
    elif event.text == '@The_Telegraph_UP_BOT OFF' and not str(user.id)=='1616976294':
        await event.reply(file='CAADBQADZwIAAlhXWFQIBfELC8_B8wI')
        return
    elif event.text == '@The_Telegraph_UP_BOT ON' and not str(user.id)=='1616976294':
        await event.reply(file='CAADBQADGwMAAgsQSFY8GdHTOnCZzAI')
        return
    if event.text =='@The_Telegraph_UP_BOT ON' and str(user.id)=='1616976294':
        bot_on=True
        await event.reply('**__hey LAKSHAN😍, I am rebooted ✅__**')
#◇──────────────────────────────────────────────────────────────────────────────────────────────────◇
    


#◇──────────────────────Start────────────────────────────────────────────────────────────────────◇
@bot.on(events.NewMessage(incoming=True))
async def start(event):
    global bot_on
    global yes
    user=await event.get_sender()
    if bot_on==True:
        pass
    else:
        return
    if yes == False and str(event.message.message) in ["/start","/start@The_Telegraph_UP_BOT"]:
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    if str(event.message.message) in ["/start","/start@The_Telegraph_UP_BOT"]:
        user=await event.get_sender()
        await bot.send_file(
            event.chat,
            file="https://telegra.ph/file/65e826e3ef92413351de9.png",
            caption=new_start.format(user.first_name,user.id),link_preview=False,buttons=[[
            Button.url("➕ Add to Group ➕",url="t.me/The_Telegraph_UP_BOT?startgroup=botstart")
        ],[
            Button.url('☘️ The SSH Store ☘️',url="t.me/SSH_Store"),
            Button.url("🔰 The VPN Stock 🔰",url="t.me/VPN_Stock")],
        [
            Button.url("👻 Single Developers ✌️", url="https://t.me/SingleDevelopers")
        ],[
            Button.url("🚀 𝙁𝙧𝙞𝙯𝙩𝙮™ 🚀", url="https://t.me/frizty_group"),
            Button.url("🌏 UNLIMITED world™ 🌏",url="t.me/UnlimitedWorldTeam")],[
            Button.inline("🆘 Help 🆘",data="help")]])
        





#◇────────────────────────Help────────────────────────────────────────────────────────────────────◇
@bot.on(events.NewMessage(incoming=True,pattern=r"/help|/help@The_Telegraph_UP_BOT"))
async def help(event):
    global bot_on
    global yes
    user=await event.get_sender()
    if bot_on==True:
        pass
    else:    
        return
    if yes == False:
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    await bot.send_file(
        event.chat,
        file='https://telegra.ph/file/eb6e30e36c5f41b01c4c5.mp4',
        caption=help_text,
        buttons=[[
            Button.url('🍀 BOT Release Post 🍀',url='https://t.me/SingleDevelopers/635')
        ],
        [Button.inline('👀 About 👀',data='about')],
        [Button.inline('⭕️ Close ⭕️',data='cls')]])



#◇────────────CallBack Query──────────────────────────────────────────────────────────────────────────◇
@bot.on(events.callbackquery.CallbackQuery(data='help'))
async def cbhelp(event):
    global bot_on
    global yes
    user=await event.get_sender()
    if bot_on==True:
        pass
    else:
        return
    if yes == False:
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    await event.edit(
        file='https://telegra.ph/file/eb6e30e36c5f41b01c4c5.mp4',
        text=help_text,
        buttons=[[
            Button.url('🍀 BOT Release Post 🍀',url='https://t.me/SingleDevelopers/635')
        ],
        [Button.inline('👀 About 👀',data='about')],
        [Button.inline('⭕️ Close ⭕️',data='cls')]])


@bot.on(events.callbackquery.CallbackQuery(data="about"))
async def cbabout(event):
    global bot_on
    global yes
    user=await event.get_sender()
    if bot_on==True:
        pass
    else:
        return
    if yes == False:
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    await event.edit(
        file="https://telegra.ph/file/fdb3b2efeb092f58e3de6.jpg",
        text='',
        buttons=[Button.url("👻 Single Developers ✌️",url='t.me/SingleDevelopers')]
    )
    await bot.forward_messages(
        event.chat,
        688,
        -1001548395355
    )

@bot.on(events.callbackquery.CallbackQuery(data='cls'))
async def cbcls(event):
    global bot_on
    global yes
    user=await event.get_sender()
    if bot_on==True:
        pass
    else:
        return
    if yes == False:
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    await event.edit(
        file='https://telegra.ph/file/37f9af643604ccbf83443.mp4',
        text='❌ Menu Closed ❌',
        buttons=[Button.inline('♻️ Open Again ♻️',data='menu')])



@bot.on(events.callbackquery.CallbackQuery(data='menu'))
async def open(event):
    global bot_on
    global yes
    user=await event.get_sender()
    if bot_on==True:
        pass
    else:
        return
    if yes == False:
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    user=await event.get_sender()
    await event.edit(
        file='https://telegra.ph/file/65e826e3ef92413351de9.png',
        text=f"""**Hello [{user.first_name}](tg://user?id={user.id})!

👻 This is a Telegraph uploader bot
for telegram.You can upload below types
to telegraph easily by using this bot 😍

👇 You can upload 👇

⭕️ Short Videos (Must be less than 5MB)
⭕️ Pictures
⭕️ Animations
⭕️ Stickers

✅ 24 hour Active ✅**

◇───────────────◇

☘️ Dҽᐯҽ𝘭๏pҽᏒ : @Lakshan_s
👻 𝚂𝚒𝚗𝚐𝚕𝚎 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛𝚜 ✌️

◇───────────────◇
""",
link_preview=False,
buttons=[[
        Button.url("➕ Add to Group ➕",url="t.me/The_Telegraph_UP_BOT?startgroup=botstart")
],[
        Button.url('☘️ The SSH Store ☘️',url="t.me/SSH_Store"),
        Button.url("🔰 The VPN Stock 🔰",url="t.me/VPN_Stock")],
    [
        Button.url("👻 Single Developers ✌️", url="https://t.me/SingleDevelopers")
    ],[
        Button.url("🚀 𝙁𝙧𝙞𝙯𝙩𝙮™ 🚀", url="https://t.me/frizty_group"),
        Button.url("🌏 UNLIMITED world™ 🌏",url="t.me/UnlimitedWorldTeam")],[
        Button.inline("🆘 Help 🆘",data="help")]])

#◇──────────────────────────────────────────────────────────────────────────────────────────────────◇




#◇───────────────────Telegraph──────────────────────────────────────────────────────────────────────◇
@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private and e.media))
async def telegraph(event):
    global bot_on
    global yes
    user=await event.get_sender()
    if bot_on==True:
        pass
    else:
        return
    if yes == False:
#       await event.reply(f"""
#       	⛔️ Access Denied ⛔️
#
#🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
#       buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
       return
    DL_path = "./downloads/"
    if not os.path.isdir(DL_path):
        os.makedirs(DL_path)
    d=await event.reply('**__🚀 Downloading File...__**')
    file_name=await bot.download_media(event.media, DL_path)
    #await d.edit("**__Uploading__ [▪️   ]**")
    #await d.edit("**__Uploading__ [▪️▪️  ]**")
    #await d.edit("**__Uploading__ [▪️▪️▪️ ]**")
    #await d.edit("**__Uploading__ [▪️▪️▪️▪️]**")
    if file_name.endswith('webp'):
            await d.edit('**__⚠️ Oops!! this is a Sticker 🤦__**')
            await asyncio.sleep(3)
            await d.edit("**Don't warry Bro😇 I can Convert it 😂**")
            await asyncio.sleep(2)
            await d.edit('**Converting⚙️**')
            await d.edit('**Converting⚙️⚙️**')
            await d.edit('**Converting⚙️⚙️⚙️**')
            await d.edit('**Converting⚙️⚙️⚙️⚙️**')
            resize_image(file_name)
    try:
        await d.edit("**__Uploading__ [▪️   ]**")
        await d.edit("**__Uploading__ [▪️▪️  ]**")
        await d.edit("**__Uploading__ [▪️▪️▪️ ]**")
        await d.edit("**__Uploading__ [▪️▪️▪️▪️]**")
        url = upload_file(file_name)[0]
    except exceptions.TelegraphException as e:
        await event.reply(file='https://telegra.ph/file/14510a5a76516ef4d718d.mp4')
        await d.edit(f'Oops {e}',buttons=[Button.inline('🆘 Get More Help 🆘',data='help')])
        os.remove(file_name)
        return
    else:
        os.remove(file_name)
        await d.edit(
            text=f'**Link ᗚ** `https://telegra.ph{url}`\n\n**@SingleDevelopers**',
            buttons=[[
                Button.url("Goto Link 🔗",url=f'https://telegra.ph{url}'),
                Button.url('Share Link 🎁',url=f"https://t.me/share/url?url=https://telegra.ph{url}")],
                [Button.url("☘️ Join US ☘️", url="https://t.me/SingleDevelopers")]])
        await bot.send_file(
            -1001724238817,
            file=f'https://telegra.ph{url}',
            caption=
f"""**Link : **`https://telegra.ph{url}`

◇───────────────◇
**from User : [{user.first_name}](tg://user?id={user.id})**
**User id :** `{user.id}`
◇───────────────◇  

**[👻 Single Developers ✌️](t.me/SingleDevelopers)**
**Upload By ᗚ @The_Telegraph_UP_BOT**

""")

            
pattern=r'/up|/tgm|/up@The_Telegraph_UP_BOT|/tgm@The_Telegraph_UP_BOT'

@bot.on(events.NewMessage(incoming=True, pattern=r"/up|/tgm|/up@The_Telegraph_UP_BOT|/tgm@The_Telegraph_UP_BOT"))
async def telegraph(event):
    global bot_on
    global yes
    user=await event.get_sender()
    if bot_on==True:
        pass
    else:
        return  
    if yes == False:
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}]({event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    DL_path = "./downloads/"
    if not os.path.isdir(DL_path):
        os.makedirs(DL_path)   
    if event.reply_to:
        rep=await event.get_reply_message()
        if rep.file:
            d=await event.reply('**__🚀 Downloading File...__**')
            file_name=await bot.download_media(rep, DL_path)
            #await d.edit("**__Uploading__ [▪️   ]**")
            #await d.edit("**__Uploading__ [▪️▪️  ]**")
            #await d.edit("**__Uploading__ [▪️▪️▪️ ]**")
            #await d.edit("**__Uploading__ [▪️▪️▪️▪️]**")
            if file_name.endswith('webp'):
                        await d.edit('**__⚠️ Oops!! this is a Sticker 🤦__**')
                        await asyncio.sleep(4)
                        await d.edit("**Don't warry Bro😇 I can Convert it 😂**")
                        await asyncio.sleep(2)
                        await d.edit('**Converting⚙️**')
                        await d.edit('**Converting⚙️⚙️**')
                        await d.edit('**Converting⚙️⚙️⚙️**')
                        await d.edit('**Converting⚙️⚙️⚙️⚙️**')
                        #await asyncio.sleep(2)
                        #await d.edit("**__Uploading__ [▪️   ]**")
                        #await d.edit("**__Uploading__ [▪️▪️  ]**")
                        #await d.edit("**__Uploading__ [▪️▪️▪️ ]**")
                        #await d.edit("**__Uploading__ [▪️▪️▪️▪️]**")
                        resize_image(file_name)
        else:
            await event.reply(file='CAADBQAD8wIAAoxwWVbPzYTA1RQhWgI')
            return await event.reply('**please reply to a media file 😡\nnot to text message 😒**')           
        try:
            
            await d.edit("**__Uploading__ [▪️   ]**")
            await d.edit("**__Uploading__ [▪️▪️  ]**")
            await d.edit("**__Uploading__ [▪️▪️▪️ ]**")
            await d.edit("**__Uploading__ [▪️▪️▪️▪️]**")
            url = upload_file(file_name)[0]

        except exceptions.TelegraphException as e:
            await event.reply(file='https://telegra.ph/file/14510a5a76516ef4d718d.mp4')
            await d.edit(f'Oops {e}',buttons=[Button.inline('🆘 Get More Help 🆘',data='help')])
            os.remove(file_name)
            return

        else:
            os.remove(file_name)
            await d.edit(
                text=f'**Link ᗚ** `https://telegra.ph{url}`\n\n**@SingleDevelopers**',
                buttons=[[
                    Button.url("Goto Link 🔗",url=f'https://telegra.ph{url}'),
                    Button.url('Share Link 🎁',url=f"https://t.me/share/url?url=https://telegra.ph{url}")],
                    [Button.url("☘️ Join US ☘️", url="https://t.me/SingleDevelopers")]])
            await bot.send_file(
            -1001724238817,
            file=f'https://telegra.ph{url}',
            caption=
f"""**Link : **`https://telegra.ph{url}`

◇───────────────◇
**from User : [{user.first_name}](tg://user?id={user.id})**
**User id :** `{user.id}`
**Chat id :** `-100{event.chat.id}`
◇───────────────◇  

**[👻 Single Developers ✌️](t.me/SingleDevelopers)**
**Upload By ᗚ @The_Telegraph_UP_BOT**

""")
    if not event.reply_to:
        await event.reply('**please reply to a media file 🥱**')
        


def resize_image(image):
    im = Image.open(image)
    tmp = im.save(image, "PNG")




@bot.on(events.NewMessage(incoming=True,pattern="/telegraph")) 
async def paste(event): 
    global yes
    global bot_on
    user=await event.get_sender()
    if bot_on==True:
        pass
    else:
        return 
    if yes == False:
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    telegraph=Telegraph() 
    #html=markdown.markdown()
    reply = await event.get_reply_message() 
 
    if not reply or not reply.text: 
        return await event.reply("Reply to a text message 💁‍♂️") 
    qwe = telegraph.create_account(short_name='Created By @Telegraph_UP_BOT') 
    r=event.text 
    eee=r.split(' ') 
    if len(eee) < 2: 
        return await event.reply("**Usage:**\n /telegraph [Page name]") 
    page_name = r.removeprefix('/telegraph ') 
    page = telegraph.create_page(page_name, html_content=(markdown.markdown(reply.text)).replace("\n", "<br>")) 
    d=page['url'] 
    print(d) 
    await event.reply( 
        f"**Posted:** `{page['url']}`", 
        buttons=[[ 
            Button.url('Goto Link 🔗',url=page['url']), 
            Button.url('Share Link 🎁',url=f'https://t.me/share/url?url={d}') 
        ],[Button.url("☘️ Join US ☘️", url="https://t.me/SingleDevelopers")]] 
    )
    await bot.send_message(
        -1001724238817,
        f"**Posted:** `{page['url']}`\n\n**Sender :** [{event.sender.first_name}](tg://user?id={event.sender_id})\n**Sender id :** {event.sender_id}",
        buttons=[[
            Button.url('Goto Link 🔗',url=page['url']),
            Button.url('Share Link 🎁',url=f'https://t.me/share/url?url={d}')
        ],[Button.url("☘️ Join US ☘️", url="https://t.me/SingleDevelopers")]]
    )
    return




@bot.on(events.NewMessage(incoming=True))
async def id(event):
    global bot_on
    global yes
    if bot_on==True:
        pass
    else:
        return
    if yes == False and str(event.message.message) == "/id":
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    if event.reply_to and str(event.message.message) == "/id":
        rep=await event.get_reply_message()
        if rep.media:
            try:
                media_id = pack_bot_file_id(rep.media)          
                await event.reply(f'**This chat id :**` {event.chat_id}`\n**User id :**` {rep.sender_id}`\n**Message id :**` {rep.id}`\n**Media id :** `{media_id}`')
            except:
                await event.reply(f'**This chat id :**` {event.chat_id}`\n**User id :**` {rep.sender_id}`\n**Message id :**` {rep.id}`')
        else:
            await event.reply(f'**This chat id :**` {event.chat_id}`\n**User id :**` {rep.sender_id}`\n**Message id :**` {rep.id}`')
    else:
        if not event.reply_to and str(event.message.message) == "/id" and not(event.is_private):
            await event.reply(f'**Your id :** `{event.sender_id}`\n**This chat id :** `{event.chat_id}`')
        if event.is_private and str(event.message.message) == "/id":
            await event.reply(f'**Your id :** `{event.sender_id}`')

@bot.on(events.NewMessage(incoming=True))
async def id(event):
    global bot_on
    global yes
    if bot_on==True:
        pass
    else:
        return
    if yes == False and str(event.message.message) == "/id":
        await event.reply(f"""
        	⛔️ Access Denied ⛔️

🙋‍♂️ Hey There [{event.sender.first_name}](tg://user?id={event.sender_id}), ☘️ I am The Telegraph Uploader BOT ☘️, You Must Join @SingleDevelopers Telegram Channel To Use This BOT. So, Please Join it & Try Again🤗. Thank You 🤝""",
        buttons=[Button.url('</> SingleDevelopers',url='https://t.me/SingleDevelopers')])
        return
    
   if str(event.message.message) == "txt":
    m = await event.reply("🖊 Writing...")
        body = {"text":f"{event.text}"}
        req = requests.post('https://api.single-developers.software/write1', headers={'Content-Type': 'application/json'}, json=body)
        pic = req.history[1].url
        await bot.send_file(
                photo=f"{pic}"
        )
   if event.repy_to and str(event.message.message) == "txt":
    msg=await event.get_reply_message()
    m = await event.reply("🖊 Writing...")
        body = {"text":f"{msg}"}
        req = requests.post('https://api.single-developers.software/write1', headers={'Content-Type': 'application/json'}, json=body)
        pic = req.history[1].url
        await bot.send_file(
                photo=f"{pic}"
        )
        
        await m.delete()

        
















print("started susccessfuly!!")
bot.start()
bot.run_until_disconnected()
