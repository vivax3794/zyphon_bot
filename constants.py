import os

cogs = ["core"]

prefix = "!"
token = os.getenv("token")

main_command_channel = int(os.getenv("command_channel"))
command_channels = [main_command_channel]