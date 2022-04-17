from dataclasses import dataclass
import discord
from discord.commands import Option
import aiohttp
from discord.ext.commands import Bot
from discord.ext import commands
import json

bot = commands.Bot()

#add your discord bot token in the string
discord_token = ""


#add your nitrado token in the string
nitrado_token = ""

@bot.slash_command()
async def unban_all(ctx: commands.Context, id: Option(str, "Enter the server id to unball all players on")):
    async with aiohttp.ClientSession() as session:
        headers = {'Authorization': nitrado_token}
        async with session.get(f"https://api.nitrado.net/services/{id}/gameservers/games/banlist", headers=headers) as response:   
            data = (await response.json())['data']['banlist']
            players = {player['name'] for player in data}
            for player in players:
                gamertag = {'identifier': player}
                async with aiohttp.ClientSession() as s:
                    async with s.delete(f"https://api.nitrado.net/services/{id}/gameservers/games/banlist", headers=headers, data=json.dumps(gamertag)) as t:  
                        await ctx.respond(t)




bot.run(discord_token)
