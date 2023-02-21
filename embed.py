import discord
from typing import Union


def send_embed(ctx, title: str, description: str = None, color: Union[int, discord.Colour, None] = 0x0391fb):
    """
    Send simple discord embed
    :param ctx: Discord ctx
    :param str title: The title of embed
    :param str description: The description of embed
    :param int,discord.Colour,None color: The color of embed
    """
    embed = discord.Embed(title=title, description=description, color=color)

    return ctx.send(embed=embed)
