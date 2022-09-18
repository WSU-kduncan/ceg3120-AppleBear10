Part 3 - R&D (Research & Documentation)

In Discord-Bot folder, add a README.md file. Document the following:

**Setup:**
- dependencies (what packages need to be installed to run the project)
  - Python 1.7.3
  - Python 2.0.1
  - pip
- how to get an API token
  - You will need to go to this link where you have your bot created: https://discord.com/developers/applications/
  - Click on your bot and go to "bot" on the left side tab
  - Where is says token simply "copy"
- where to put it to work with the code
  - You will need to put it in a .env file with the following edit
  - DISCORD_TOKEN="token copied"

**Usage**
- with your changes to the code in place, describe
- what commands you can type in your Discord server
- what response this will provide (from your bot)
   - I changed each string in the array with custom quotes
   - the command is applebear!
![](https://cdn.discordapp.com/attachments/194319856009478145/1021144130287587348/unknown.png)
**Research**
- you may have realized that it is lame that the bot only runs when you run the program - it turns off if you disconnect or need to switch tasks
- In the real world, things are "always on", not waiting for Bob to turn his PC on and make sure the program is running
- Research some possible solutions that would solve this, and discuss why you think it would work
  - One way to keep a discord bot on is to host the script on a server at all times
  - You can actually purchase a VPS (Virtual Private Server) for the bot to be hosted on and it will run at all times

  - Another way is to get a rasperry pi
  - It's essentially a mini computer that you could purchase for $50
  - Uses alot less power and has less advanced hardware but sufficient enough for a discord bot
  - You can also install an OS on there therefore Linux and be able to use it
