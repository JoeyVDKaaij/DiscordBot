import discord
from discord import app_commands
from discord.ext import commands
import os
import sys
import random
import friendlist

import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        if response != '':
            await message.author.send(response) if is_private else await message.channel.send(response)
            if response == 'You\'ve shot Joey\'s laptop! Congratulations!! \n https://tenor.com/view/bsod-gif-26376970':
                quit()

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = os.getenv('Discord_Bot_Token')
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)!")
        except Exception as e:
            print(e)

    @bot.tree.command(name="help", description="See all the commands that the bot has for more technical purposes.")
    async def help(interaction: discord.Interaction):
        await interaction.response.send_message(f"Here are some of the more general and/or technical commands:\n"
                                                f"- send \"joinvc\" to make the bot join the voice channel that you are currently in."
                                                f"- send \"leavevc\" to make the bot leave the voice channel that it is currently in.",
                                                ephemeral=True)

    @bot.tree.command(name="activityhelp", description="See all the commands for the current activity (if active)!")
    async def activityhelp(interaction: discord.Interaction):
        await interaction.response.send_message(f"Here are the following commands for the activity FNAF ULTIMATE CUSTOM NIGHT:\n"
                                                f"- send \"left door\" to close/open the left door.\n"
                                                f"- send \"right door\" to close/open the right door.\n"
                                                f"- send \"middle vent\" to close/open the middle vent.\n"
                                                f"- send \"right vent\" to close/open the right vent.\n"
                                                f"- send \"camera\" to open/close the camera.\n"
                                                f"- send \"flashlight\" to activate the flashlight for 3 seconds.\n"
                                                f"- send \"all off\" to turn everything off (beside the flashlight, doors, vents and mask).\n"
                                                f"- send \"catch that fish\" to attempt to catch a fish from old man consequence.\n"
                                                f"- send \"fuck them ads\" to close the ads.\n"
                                                f"- send \"i have fans\" to activate/disable the fan.\n"
                                                f"- send \"fuck this\" to go back to the main menu (You are evil if you do this).\n"
                                                f"- send \"power generator\" to activate/disable the power generator.\n"
                                                f"- send \"silent ventilation\" to activate/disable the silent ventilation.\n"
                                                f"- send \"heater\" to activate/disable the heater.\n"
                                                f"- send \"power ac\" to activate/disable the power ac.\n"
                                                f"- send \"global music box\" to activate/disable the global music box.\n"
                                                f"- send \"mouse up\" to move the mouse upwards.\n"
                                                f"- send \"mouse down\" to move the mouse downwards.\n"
                                                f"- send \"mouse left\" to move the mouse left.\n"
                                                f"- send \"mouse right\" to move the mouse right.\n"
                                                f"Don't send these commands with a / nor between \"\" (The \"\" was there to make the command more understandable). It's also NOT case-sensitive. For more information contact @MinyJo", ephemeral=True)

    @bot.tree.command(name="funnyhelp", description="See all the commands for the funny stuff")
    async def funnyhelp(interaction: discord.Interaction):
        await interaction.response.send_message(f"Here are the following funny commands!\n"
                                                f"These are the specific commands! You have to specifically send this for it to work:"
                                                f"- send \"hi\" or \"hello\" and the bot will say hi back.\n"
                                                f"- send \"roll\" to roll between 1 to 6.\n"
                                                f"- send \"fuck you\" for an agressive fuck you back!.\n"
                                                f"- send \"can you work?\" to hear how to bot declines.\n"
                                                f"- send \"meow\" for an meow back.\n"
                                                f"- send \"good morning\" for a good morning back.\n"
                                                f"These are the less-specific commands! You have to include these words anywhere in your message for this to work:"
                                                f"- send \"cuh\" and the bot will be saying ON GOD.\n"
                                                f"- send \"potato\" for potato.\n"
                                                f"- send \"🥔\" for :potato:.\n"
                                                f"- send \"eepy\" for good night.\n"
                                                f"- send \"hihi\" for HIHI.\n"
                                                f"- send \"fym\" and the bot fucked your mom.\n"
                                                f"- send \"yippee\" for YIPPEE.\n"
                                                f"- send \"yo\" for yo.\n"
                                                f"Don't send these commands with a / nor between \"\" (The \"\" was there to make the command more understandable). It's also NOT case-sensitive. Some commands are not shown but you can try to activate them if you are that smart. For more information contact @MinyJo",
                                                ephemeral=True)

    @bot.tree.command(name="whos_joeys_favorite_friend", description="See who\'s Joey\'s favorite friend!!")
    async def whosjoeysfavoritefriend(interaction: discord.Interaction):
        randomintergure = random.randint(0, 29)
        bestie = friendlist.NameGetter(randomintergure)
        await interaction.response.send_message(f"Joey's best friend is: {bestie}!!!")

    pingSpam = 10

    @bot.tree.command(name="pingsomeone", description=f'Ping Joey a certain amount (max {pingSpam})!')
    @app_commands.describe(person = "Who has to be pinged", amount = "How many times this person should be pinged")
    async def pingsomeone(interaction: discord.Interaction, person : str, amount : int):
        if amount > 0:
            if amount > pingSpam:
                amount = pingSpam

            await interaction.response.defer()
            for i in range(amount):
                await interaction.followup.send(person)
        else:
            await interaction.response.send_message("Amount cannot be 0 or lower!", ephemeral=True)

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" in the channel: {channel}')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    # intents = discord.Intents.default()
    # intents.members = True

    client = commands.Bot(command_prefix='!', intents=intents)

    @bot.tree.command(name="join", description=f'Have the bot join the voice channel that you are currently in.')
    async def join(interaction: discord.Interaction):
        print(f'Its going through the command.')
        if (interaction.user.voice):
            channel = interaction.user.voice.channel
            await channel.connect()
        else:
                await interaction.response.send_message("Mf you aint even in a voice channel?!?!?!")

    @client.command(pass_context=True)
    async def leave(ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I have left the voice channel.")
        else:
            await ctx.send("I am currently not in a voice channel.")

    bot.run(TOKEN)