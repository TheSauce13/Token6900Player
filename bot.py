from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    MenuButtonWebApp
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)
import os

# ✅ Load from .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ✅ Read BOT_TOKEN from environment
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN is not set in environment variables.")

# ✅ CONFIGURATION
MINI_APP_URL = "https://thesauce13.github.io/Miniplayer/"
BOT_LINK = "https://t.me/Token6900PlayerBot"

WEBSITE_URL = "https://token6900.com/"
X_URL = "https://x.com/token_6900"
INSTAGRAM_URL = "https://instagram.com/token_6900"

TOKEN_NAME = "Token 6900 🎵"

VIDEO_URL = "https://token6900.com/assets/images/banner-vdo.mp4"

# ✅ /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat

    if chat.type == "private":
        # 1️⃣ Set persistent menu button
        await context.bot.set_chat_menu_button(
            chat_id=chat.id,
            menu_button=MenuButtonWebApp(
                text=TOKEN_NAME,
                web_app=WebAppInfo(url=MINI_APP_URL)
            )
        )

        # 2️⃣ Send video with caption
        await update.message.reply_video(
            video=VIDEO_URL,
            caption="🐬 Welcome to Token 6900 🎵"
        )

        # 3️⃣ Send info card
        await update.message.reply_text(
            text=(
                f"🌐  W: {WEBSITE_URL}\n"
                f"📡  X: {X_URL}\n"
                f"📸  I: {INSTAGRAM_URL}"
            )
        )

    else:
        # Group chat – send inline button linking to bot
        keyboard = [
            [InlineKeyboardButton(
                text=TOKEN_NAME,
                url=BOT_LINK
            )]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            text="🔥 TOKEN 6900 Player is Live!\n\nTap below to launch in Telegram:",
            reply_markup=reply_markup
        )

# ✅ /website command
async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WEBSITE_URL)

# ✅ /x command
async def x(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(X_URL)

# ✅ /instagram command
async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(INSTAGRAM_URL)

# ✅ /dolphin command
async def dolphin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🐬 Token 6900 🐬")

# ✅ /links command
async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text=(
            "░░░🐬 𝕋𝕆𝕂𝔼ℕ 𝟞𝟡𝟘𝟘 🐬░░░\n\n"
            f"🌐  W: {WEBSITE_URL}\n"
            f"📡  X: {X_URL}\n"
            f"📸  I: {INSTAGRAM_URL}"
        )
    )

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("website", website))
    app.add_handler(CommandHandler("x", x))
    app.add_handler(CommandHandler("instagram", instagram))
    app.add_handler(CommandHandler("dolphin", dolphin))
    app.add_handler(CommandHandler("links", links))
    print("✅ Bot is running. Press CTRL+C to stop.")
    app.run_polling()
