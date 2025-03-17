import mineflayer
import logging
bot = mineflayer.Bot(username="snark", offline=True, log_level=logging.ERROR, log_file="log.txt")

@bot.event
async def on_spawn(*args):
    print("Spawned!")
@bot.event
async def on_chat(username, message, *args): # why tf is username returning user info tf
    # print(f"{username}: {message}")
    logging.log(logging.DEBUG, f"{username}: {message}")
bot.run("localhost", 25565)