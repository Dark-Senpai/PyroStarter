from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from Config import configure 
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# necessary to define Client 
code = Client(
  'kai84',
  bot_token=Config.BOT_TOKEN,
  api_id=Config.API_ID,
  api_hash=Config.API_HASH
)

# the start message code 
@code.on_message(filters.command(["start"]))
async def start_message(client, message):
  start = f"`Hello {message.from_user.username}-kun` \n\nI am a active! 😁😁"
  message.send_message(
    text=start,
    quote=False,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("Dev", url="https://t.me/Parth_Senpai")
        ],
      ],
    ),
  )
