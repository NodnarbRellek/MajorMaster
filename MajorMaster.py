import discord

client = discord.Client()

cadOG = []
scobOG = []
gccisOG = []
kgcoeOG = []
cetOG= []
chstOG = []
colaOG = []
cosOG = []
ntidOG = []

OGlist = [cadOG, scobOG, gccisOG, kgcoeOG, cetOG, chstOG, colaOG, cosOG, ntidOG]


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Major Master"))
    fn = "Majors.txt"
    index = 0
    fd = open(fn)
    for line in fd:
        line = line.strip()
        if line == "-":
            index += 1
        else:
            OGlist[index].append(line)
    fd.close()


@client.event
async def on_message(message):
    if message.author.id == 99999999999:  # Replace with owner or admin ID
        server = message.guild
        masterlistObject = server.roles
        verifier = []
        for item in masterlistObject:
            verifier.append(item.name.lower())
        if message.content.strip() == "createAlltheRoles":
            sayChannel = message.channel
            await sayChannel.send("Creating all missing roles...")

            colleges = {'cad': discord.colour.Color.teal(), 'scob': discord.colour.Color.purple(), 'gccis': discord.colour.Color.blue(),
                        'kgcoe': discord.colour.Color.red(), 'cet': discord.colour.Color.dark_blue(), 'chst': discord.colour.Color.dark_purple(),
                        'cola': discord.colour.Color.gold(), 'cos': discord.colour.Color.dark_magenta(), 'ntid': discord.colour.Color.green(),
                        'ue': discord.colour.Color.magenta()}
            for college, color in colleges.items():
                if college not in verifier:
                    isUE = (college == 'ue')  # Only UE role is pingable. Will be false otherwise.
                    await server.create_role(name=college.upper(), mentionable=isUE, colour=color)

            for item in OGlist:
                for major in item:
                    if major.lower() not in verifier:
                        await server.create_role(name=major, mentionable=True)  # Set to false to remove @ing

            await sayChannel.send("All roles ready for use")
    if message.channel.id == 999999999999999 and message.author != client.user:  # Replace with role add channel ID
        sayChannel = message.channel
        statement = message.content.strip().split()
        command = statement[0]
        server = message.guild
        togive = None
        try:
            if command.lower().strip() == "add":
                if len(message.content) >= 4:
                    rest = message.content.strip()[4:]
                else:
                    return
                masterlist = server.roles
                for item in masterlist:
                    if item.name == "CAD":
                        cad = item
                    elif item.name == "SCOB":
                        scob = item
                    elif item.name == "GCCIS":
                        gccis = item
                    elif item.name == "KGCOE":
                        kgcoe = item
                    elif item.name == "CET":
                        cet = item
                    elif item.name == "CHST":
                        chst = item
                    elif item.name == "COLA":
                        cola = item
                    elif item.name == "NTID":
                        ntid = item
                    elif item.name == "COS":
                        cos = item
                    if item.name.lower() == rest.lower():
                        togive = item

                if togive is None:
                    await sayChannel.send("The role " + rest + " does not exist. say \"roles\" to see all roles")
                    return
                majorValid = False
                index = 0
                for college in OGlist:
                    for major in college:
                        if rest.lower().strip() == major.lower():
                            majorValid = True
                            if index == 0:
                                await message.author.add_roles(togive, cad)
                                await sayChannel.send(
                                    "The role " + togive.name + " has been granted along with your college")
                            if index == 1:
                                await message.author.add_roles(togive, scob)
                                await sayChannel.send(
                                    "The role " + togive.name + " has been granted along with your college")
                            if index == 2:
                                await message.author.add_roles(togive, gccis)
                                await sayChannel.send(
                                    "The role " + togive.name + " has been granted along with your college")
                            if index == 3:
                                await message.author.add_roles(togive, kgcoe)
                                await sayChannel.send(
                                    "The role " + togive.name + " has been granted along with your college")
                            if index == 4:
                                await message.author.add_roles(togive, cet)
                                await sayChannel.send(
                                    "The role " + togive.name + " has been granted along with your college")
                            if index == 5:
                                await message.author.add_roles(togive, chst)
                                await sayChannel.send(
                                    "The role " + togive.name + " has been granted along with your college")
                            if index == 6:
                                await message.author.add_roles(togive, cola)
                                await sayChannel.send(
                                    "The role " + togive.name + " has been granted along with your college")
                            if index == 7:
                                await message.author.add_roles(togive, cos)
                                await sayChannel.send(
                                    "The role " + togive.name + " has been granted along with your college")
                            if index == 8:
                                await message.author.add_roles(togive, ntid)
                                await sayChannel.send(
                                    "The role " + togive.name + " has been granted along with your college")
                    index += 1
                if not majorValid:
                    await message.author.add_roles(togive)
                    await sayChannel.send("The role " + togive.name + " has been granted")
            if command.lower().strip() == "remove":
                masterlist = server.roles
                if len(message.content) >= 7:
                    rest = message.content.strip()[7:]
                else:
                    return
                totake = None
                for item in masterlist:
                    if item.name.lower() == rest.lower():
                        totake = item
                if totake is None:
                    await sayChannel.send("The role " + rest + " does not exist")
                    return
                await message.author.remove_roles(totake)
                await sayChannel.send("The role " + totake.name + " has been removed")
            if command.lower().strip() == "roles":
                masterlist = server.roles
                for item in masterlist:
                    if item.name == "CAD":
                        cad = item
                    elif item.name == "SCOB":
                        scob = item
                    elif item.name == "GCCIS":
                        gccis = item
                    elif item.name == "KGCOE":
                        kgcoe = item
                    elif item.name == "CET":
                        cet = item
                    elif item.name == "CHST":
                        chst = item
                    elif item.name == "COLA":
                        cola = item
                    elif item.name == "NTID":
                        ntid = item
                    elif item.name == "COS":
                        cos = item
                payload = []
                gotlist = []
                nonCollege = []
                cadEmbed = discord.Embed()
                cadEmbed.title = "College of Art and Design"
                cadEmbed.colour = cad.colour
                cadEmbed.description = "CAD\n"
                gotlist.append("CAD")
                for major in OGlist[0]:
                    cadEmbed.description += major + "\n"
                    gotlist.append(major)
                payload.append(cadEmbed)

                scobEmbed = discord.Embed()
                scobEmbed.title = "Saunders College of Business"
                scobEmbed.colour = scob.colour
                scobEmbed.description = "SCOB\n"
                gotlist.append("SCOB")
                for major in OGlist[1]:
                    scobEmbed.description += major + "\n"
                    gotlist.append(major)
                payload.append(scobEmbed)

                gccisEmbed = discord.Embed()
                gccisEmbed.title = "Golisano College of Computing and Information Sciences"
                gccisEmbed.colour = gccis.colour
                gccisEmbed.description = "GCCIS\n"
                gotlist.append("GCCIS")
                for major in OGlist[2]:
                    gccisEmbed.description += major + "\n"
                    gotlist.append(major)
                payload.append(gccisEmbed)

                kgcoeEmbed = discord.Embed()
                kgcoeEmbed.title = "Kate Gleason College of Engineering"
                kgcoeEmbed.colour = kgcoe.colour
                kgcoeEmbed.description = "KGCOE\n"
                gotlist.append("KGCOE")
                for major in OGlist[3]:
                    kgcoeEmbed.description += major + "\n"
                    gotlist.append(major)
                payload.append(kgcoeEmbed)

                cetEmbed = discord.Embed()
                cetEmbed.title = "College of Engineering Technology"
                cetEmbed.colour = cet.colour
                cetEmbed.description = "CET\n"
                gotlist.append("CET")
                for major in OGlist[4]:
                    cetEmbed.description += major + "\n"
                    gotlist.append(major)
                payload.append(cetEmbed)

                chstEmbed = discord.Embed()
                chstEmbed.title = "College of Health Sciences and Technology"
                chstEmbed.colour = chst.colour
                chstEmbed.description = "CHST\n"
                gotlist.append("CHST")
                for major in OGlist[5]:
                    chstEmbed.description += major + "\n"
                    gotlist.append(major)
                payload.append(chstEmbed)

                colaEmbed = discord.Embed()
                colaEmbed.title = "College of Liberal Arts"
                colaEmbed.colour = cola.colour
                colaEmbed.description = "COLA\n"
                gotlist.append("COLA")
                for major in OGlist[6]:
                    colaEmbed.description += major + "\n"
                    gotlist.append(major)
                payload.append(colaEmbed)

                cosEmbed = discord.Embed()
                cosEmbed.title = "College of Science"
                cosEmbed.colour = cos.colour
                cosEmbed.description = "COS\n"
                gotlist.append("COS")
                for major in OGlist[7]:
                    cosEmbed.description += major + "\n"
                    gotlist.append(major)
                payload.append(cosEmbed)

                ntidEmbed = discord.Embed()
                ntidEmbed.title = "National Technical Institute for the Deaf"
                ntidEmbed.colour = ntid.colour
                ntidEmbed.description = "NTID\n"
                gotlist.append("NTID")
                for major in OGlist[8]:
                    ntidEmbed.description += major + "\n"
                    gotlist.append(major)
                payload.append(ntidEmbed)

                other = discord.Embed()
                other.title = "Other Roles"
                other.colour = discord.colour.Color.orange()
                other.description = ""
                foundBot = False
                masterlistb = reversed(masterlist)
                for item in masterlistb:
                    if not foundBot:
                        if item.name == "Bot":
                            foundBot = True
                        continue
                    if item.name not in gotlist and item.name != "@everyone":
                        nonCollege.append(item.name)
                for role in nonCollege:
                    other.description += role + "\n"
                payload.append(other)

                for displayItem in payload:
                    await sayChannel.send(embed=displayItem)

            if command.lower().strip() == "help":
                helpEmbed = discord.Embed()
                helpEmbed.title = "Help"
                helpEmbed.type = "rich"
                helpEmbed.colour = discord.colour.Color.green()
                helpEmbed.add_field(name="\"add <major>\"", value="adds a major and the associated college", inline=False)
                helpEmbed.add_field(name="\"add <role>\"", value="adds any role", inline=False)
                helpEmbed.add_field(name="\"remove <role>\"", value="removes a role", inline=False)
                helpEmbed.add_field(name="\"roles\"", value="see all roles", inline=False)
                await sayChannel.send(embed=helpEmbed)

        except discord.DiscordException:
            await sayChannel.send("This operation can not be performed")


client.run('99999999999999') #replace with API key
