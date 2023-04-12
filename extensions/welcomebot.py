import discord
from discord.ext import commands

class WelcomeBot(commands.Cog):

    new_member_role_name = "New Member"

    def __init__(self, bot):
        self.bot = bot

    async def setup_role(self):
        exists = False
        for role in await self.bot.guilds[0].fetch_roles():
            if role.name == self.new_member_role_name:
                exists = True
                break
        if exists:
            return

        permissions = discord.Permissions.none()
        permissions.view_channel = True

        await self.bot.guilds[0].create_role(
            name=self.new_member_role_name,
            color=discord.Color.red(),
            hoist=True,
            permissions = permissions
        )


async def setup(bot):
    welcome_bot = WelcomeBot(bot)
    await bot.add_cog(welcome_bot)
    await welcome_bot.setup_role()
