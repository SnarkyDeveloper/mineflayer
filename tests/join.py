import prism

bot = prism.Bot(username="SnarkyDev", offline=True)

@bot.event
async def on_spawn(*args):
    with open('tests/join.txt', 'w', encoding='utf-8', errors='ignore') as f:
        f.write(str(args))
    print("Spawned!")
    
bot.run("localhost", 25565)

