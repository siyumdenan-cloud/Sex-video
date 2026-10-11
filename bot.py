
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# Apna Telegram Bot Token yahan dalo
BOT_TOKEN = "8840094189:AAHvuZWuSB8jjZkklfFaUIcmld0trMFNBRQ"

logging.basicConfig(level=logging.INFO)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "🤖 Telegram Profile Checker\n\n"
        "Commands:\n"
        "/check @username\n\n"
        "Note: Private phone number access nahi hota."
    )


async def check(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if not context.args:
        await update.message.reply_text(
            "Usage: /check @username"
        )
        return

    username = context.args[0].lstrip("@")

    if not username:
        await update.message.reply_text(
            "Valid username dalo."
        )
        return

    try:
        chat = await context.bot.get_chat(username)

        name = chat.full_name or "Not available"
        user_name = (
            f"@{chat.username}"
            if chat.username
            else "Not available"
        )

        result = (
            "✅ Public Profile Found\n\n"
            f"👤 Name: {name}\n"
            f"🔹 Username: {user_name}\n"
            f"🆔 Telegram ID: {chat.id}\n\n"
            "📱 Phone Number: Private\n"
            "Username se private number nahi milta."
        )

        await update.message.reply_text(result)

    except Exception:
        await update.message.reply_text(
            "❌ Profile nahi mili ya access available nahi hai."
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check", check))

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
  
