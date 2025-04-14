import os
import asyncio
from bot import LeaderboardBot
from database.models import Base, engine


async def main():
    # Ensure the `teams` table is created
    Base.metadata.create_all(bind=engine)
    
    # Initialize bot
    bot = LeaderboardBot()
    
    # Load cogs
    await bot.load_extension('cogs.leaderboard_commands')
    
    # Start bot
    async with bot:
        await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())
