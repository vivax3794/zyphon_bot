import constants

async def in_command_cahnnel(ctx):
    return ctx.channel.id in constants.command_channels