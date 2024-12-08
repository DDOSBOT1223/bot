import random
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the characters to choose from (only hex characters '0-9' and 'a-f')
HEX_CHARACTERS = '0123456789abcdef'

# Function to generate random hex string with the specified characters
def generate_random_hex() -> str:
    # Generate 24 random bytes (48 characters in hex format)
    random_bytes = [random.choice(HEX_CHARACTERS) for _ in range(48)]  # 48 characters = 24 bytes
    hex_string = ''.join(random_bytes)
    # Format the string to match the \x.. style (e.g., \x9a\xe3\xdb...)
    formatted_hex_string = '\\x' + '\\x'.join([hex_string[i:i+2] for i in range(0, len(hex_string), 2)])
    return formatted_hex_string

# Command handler for the '/start' command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Use /generate to get a random hex string.')

# Command handler for the '/generate' command
def generate(update: Update, context: CallbackContext):
    random_hex = generate_random_hex()
    update.message.reply_text(f'Generated Hex String: {random_hex}')

def main():
    # Telegram Bot Token (replace with your actual bot token)
    bot_token = 'YOUR_BOT_TOKEN'

    # Create Updater and pass it your bot's token.
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('generate', generate))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
    