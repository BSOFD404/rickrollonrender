import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Replace with your actual values
BOT_TOKEN = "7719637928:AAFsQ6QHSH7z_GUeu6HMYl62yngKQPsRL_g"
ADMIN_USER_ID = 6013637983  # Replace with your Telegram user ID (as an integer)

rickroll_count = 0  # Global variable to store the rickroll count

async def many(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the current rickroll count."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Rickrolled count: {rickroll_count}")

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Resets the rickroll count (only for the admin)."""
    global rickroll_count  # Access the global variable
    user_id = update.effective_user.id

    if user_id == ADMIN_USER_ID:
        rickroll_count = 0
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Rickroll count reset!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="You are not authorized to use this command.")

def main() -> None:
    """Starts the Telegram bot."""
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("many", many))
    application.add_handler(CommandHandler("reset", reset))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()

# Function to increment the rickroll count (called from the web server)
def increment_rickroll_count():
    global rickroll_count
    rickroll_count += 1
    print(f"Rickroll count incremented to: {rickroll_count}")
