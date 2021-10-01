# ModMail
A simple mailbox for your server

## Setup

In the modmail command has 2 lines where changes are needed

```py
guild = client.get_guild(id=id_guild)
guild_channel = client.get_channel(id_channel)
```

Substitute `id_guild` for your server id
Replace `id_channel` for ModMail chat id

In the last line we have:

```py
client.run('Token here')
```

Replace the `Token here` for your bot's token

Required dependencies:
[Discord.py](https://discordpy.readthedocs.io/)

To install dependencies, open cmd and type:
```py
pip install discord.py
```

## Commands

There is only one command.

Go to the DM of your modmail bot and type:

```py
-modmail
```

After that a support request will be sent to modmail chat.
