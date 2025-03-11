import mineflayer

bot = mineflayer.Bot(username="SnarkyDev", offline=True)

@bot.event
async def on_spawn(*args):
    print("Spawned!")
    
bot.run("localhost", 25565)

