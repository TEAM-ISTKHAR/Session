from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import START_IMG, OWNER_ID, SUPPORT_CHAT, UPDATE_CHANNEL

# Custom Filters
def filter_cmd(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter_cmd("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention

    START_TXT = f"""**◈ ʜᴇʏ ʙᴧʙʏ {msg.from_user.mention}  ✤,

◈ ɪ ᴧᴍ {me2},

◈ ᴧɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴧᴛᴏʀ ʙᴏᴛ - ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏꜰ ᴩʏʀᴏɢʀᴧᴍ.

◈ ᴘʟᴇᴧꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴧʀʏ ʏᴏᴜ ᴡᴧɴᴛ ᴛᴏ ɢᴇɴᴇʀᴧᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

◈ ɪꜰ ʏᴏᴜ ɴᴇᴇᴅ ᴧɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ !**"""

    START_BTN = [
        [InlineKeyboardButton("ɢᴇɴᴇʀᴧᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
        ],
        [InlineKeyboardButton("ɢᴜɪᴅᴇ", callback_data="guide")]
    ]

    await bot.send_photo(
        chat_id=msg.chat.id,
        photo=START_IMG,
        caption=START_TXT,
        reply_markup=InlineKeyboardMarkup(START_BTN),
    )


GUIDE_TXT = """**◈ ʙᴧsɪᴄ ᴄᴏᴍᴍᴀɴᴅs

➻ ᴛʏᴘᴇ /gen ᴏʀ ᴛᴀᴘ ɢᴇɴᴇʀᴧᴛᴇ sᴇssɪᴏɴ ꜰᴏʀ ɢᴇɴ sᴇssɪᴏɴ.

➻ ᴛʏᴘᴇ /ping ᴄʜᴇᴄᴋ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ

➻ ᴛʏᴘᴇ /stats ꜰᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ sᴛᴧᴛs (ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴧɴ ᴜsᴇ)

➻ ᴛʏᴘᴇ /broadcast ᴛᴏ sᴇɴᴅ ᴧ ᴍᴇssᴧɢᴇ ᴛᴏ ᴧʟʟ ᴜsᴇʀs + ᴄʜᴧᴛs (ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴧɴ ᴜsᴇ)

⦿ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ꜰᴏʀ ᴍᴏʀᴇ ᴜᴘᴅᴧᴛᴇs.**"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data

    if data == "guide":
        await query.message.edit_text(
            text=GUIDE_TXT,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
                    InlineKeyboardButton("ᴜᴘᴅᴧᴛᴇs", url=f"https://t.me/{UPDATE_CHANNEL}"),
                ],
                [InlineKeyboardButton("⬅️ ʙᴧᴄᴋ", callback_data="start_menu")]
            ])
        )

    elif data == "start_menu":
        me2 = (await client.get_me()).mention

        START_TXT = f"""**◈ ʜᴇʏ ʙᴧʙʏ {query.from_user.mention}  ✤,

◈ ɪ ᴧᴍ {me2},

◈ ᴧɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴧᴛᴏʀ ʙᴏᴛ - ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏꜰ ᴩʏʀᴏɢʀᴧᴍ.

◈ ᴘʟᴇᴧꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴧʀʏ ʏᴏᴜ ᴡᴧɴᴛ ᴛᴏ ɢᴇɴᴇʀᴧᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

◈ ɪꜰ ʏᴏᴜ ɴᴇᴇᴅ ᴧɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ !**"""

        START_BTN = [
            [InlineKeyboardButton("ɢᴇɴᴇʀᴧᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
            [
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
                InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            ],
            [InlineKeyboardButton("ɢᴜɪᴅᴇ", callback_data="guide")]
        ]

        try:
            await query.message.edit_caption(
                caption=START_TXT,
                reply_markup=InlineKeyboardMarkup(START_BTN)
            )
        except:
            await query.message.edit_text(
                text=START_TXT,
                reply_markup=InlineKeyboardMarkup(START_BTN)
            )
