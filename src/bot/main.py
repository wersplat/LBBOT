import discord
from discord.ext import commands
from config import discord_bot_token, target_channel_id

# Initialize bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready and logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Ensure the bot doesn't respond to its own messages
    if message.author == bot.user:
        return

    # Check if the message is in the target channel and contains an attachment
    if str(message.channel.id) == target_channel_id and message.attachments:
        for attachment in message.attachments:
            if attachment.content_type.startswith("image/"):
                await message.channel.send("Image received! Processing...")
                # Placeholder for OCR processing logic
                # result = parse_screenshot(attachment)
                await message.channel.send("Processing complete! (OCR logic not implemented yet)")

# Run the bot
bot.run(discord_bot_token)
