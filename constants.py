import os

cogs = ["core"]

prefix = "!"
token = os.getenv("TOKEN")

main_command_channel = int(os.getenv("command_channel"))

print(token)
print(main_command_channel)

command_channels = [main_command_channel]