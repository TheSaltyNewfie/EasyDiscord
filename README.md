# EasyDiscord
This is a module for python that has definitions in it to help people code a Discord bot within python.
# Who can use this?
Anyone can! This module is meant for people who are new to python or the Discord API itself and for people who are experienced and just want to make their code more pretty.
# Why did you make this module?
I wanted to rewrite my current bot and have less lines to make it more understandable and I thought it would be good to release to the public.
# Installation Tutorial
All you need to do is drag and drop the `EasyDiscord.py` into your project then you import it with `import EasyDiscord` 
Its as simple as that!

# Update: 7/12/2021
What Changed?
-------------

- This is probably the smallest update ive done for this repository
    - The GUI button to send a command is now bound to the return key

# Update: 6/19/2021
What Changed?
-------------

- now the logging doesnt indent the `message:` and `Date/Time:` lines
    - Before:
        - ![LoggingV1](https://cdn.discordapp.com/attachments/832275753793224724/855897065783164938/1MessageLoggingBefore.PNG)
    - After:
        - ![LoggingV2](https://cdn.discordapp.com/attachments/832275753793224724/855893629087514654/1MessageLoggingRedone.PNG)

- `guildMembers` `announceServer` and `consoleGUI` No longer need `IntentsName`


# Update: 6/17/2021


This update adds a few new features such as a GUI.
**The GUI should be threaded in your bot noted by the example below.**

`t1 = threading.Thread(target=ed.consoleGUI, args=[client, guild, intents])`


I have also added a feature to log messages.

![This shows the user being logged and what channel they wrote in.](https://media.discordapp.net/attachments/832275753793224724/854933196625149992/LoggingMessagesEdited.png)