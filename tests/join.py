import mineflayer
import logging
logging.basicConfig(level=logging.ERROR, filename="log.txt")
bot = mineflayer.Bot(username="snark", offline=True)

@bot.event
async def on_spawn(*args):
    print("Spawned!")
@bot.event
async def on_chat(username, message, thing, *args): # why tf is username returning user info tf
    print(f"{message}: {thing}")
bot.run("localhost", 25565)