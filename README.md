
# Mineflayer

A simple python wrapper around the [mineflayer project](https://github.com/PrismarineJS/mineflayer/)

License: [MIT](https://choosealicense.com/licenses/mit/)

## Installation

Installation is easy as one package install. (Ensure node.js is installed.)

```bash
  pip install mineflayer
```

## Usage/Examples

Simple bot that just joins a server.

```python
import mineflayer

bot = mineflayer.Bot(username="SnarkyDev", offline=True)

@bot.event
async def on_spawn():
    print("Spawned!")
    
bot.run("localhost", 25565)
```

## Features

- Create a bot easily
- Discord.py format (easy to learn)
- Extensive documentation (WIP)

## Roadmap

- More events
- Finish off with all bot methods
- Documentation

## Acknowledgements

- [@customcapes](https://http://discord.com/users/848631452638642198) Awesome dude who gave up the name "mineflayer" on pypi for this project :)

## Authors

- [@SnarkyDev](https://www.github.com/SnarkyDeveloper) | Developed The Actual Package
- [@PrismarineJS](https://github.com/PrismarineJS/) | Created the mineflayer JS Package
- [@extremeheat](https://github.com/extremeheat) | Made [JSPyBridge](https://github.com/extremeheat/JSPyBridge), which is what this project mainly uses in the backend.
