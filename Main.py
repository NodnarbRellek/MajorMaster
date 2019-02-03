import discord

client = discord.Client()

cad1 = []
scob1 = []
gccis1 = []
kgcoe1 = []
cet1= []
chst1 = []
cola1 = []
cos1 = []
ntid1 = []

masterlist1 = [cad1, scob1, gccis1, kgcoe1, cet1, chst1, cola1, cos1, ntid1]

masterlist = []

server = None


@client.event
async def on_ready():

    await client.change_presence(game=discord.Game(name="Major Master"))
    fn = "Majors.txt"
    index = 0
    fd = open(fn)
    for line in fd:
        line = line.strip()
        if line == "-":
            index += 1
        else:
            masterlist1[index].append(line)
    fd.close()
@client.event
async def on_member_join(member):
    await client.send_message(member, "Reply with one of the following:\nadd *major*\nremove *major*")
    server = member.server
    masterlist = server.roles


@client.event
async def on_message(message):
    if message.server is not None and message.author.id == '0':  # replace 0 with your id
        server = message.server
        masterlist = server.roles
        if message.content.strip() == "createAlltheRoles":
            index = 0
            for item in masterlist1:
                for major in item:
                    await client.create_role(message.server, name=major)
                index += 1
    if message.server is not None and message.channel.id == '0':  # Channel ID for role channel
        server = message.server
        statement = message.content.strip().split()
        masterlist = server.roles
        command = statement[0]
        if command.lower().strip() == "add":
            rest = message.content.strip()[4:]
            index = 0
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
                elif item.name.lower() == rest.lower():
                    tempUser = message.author
                    togive = item
                    # await client.add_roles(tempUser,item)
                    await client.send_message(message.channel, "The role " + item.name + " has been granted along with your college")
            if rest != "UE":
                for item2 in masterlist1:
                    for major in item2:
                        if rest.lower() == major.lower():
                            if index == 0:
                                await client.add_roles(tempUser,togive, cad)
                            elif index == 1:
                                await client.add_roles(tempUser, togive, scob)
                            elif index == 2:
                                await client.add_roles(tempUser, togive, gccis)
                            elif index == 3:
                                await client.add_roles(tempUser, togive, kgcoe)
                            elif index == 4:
                                await client.add_roles(tempUser, togive, cet)
                            elif index == 5:
                                await client.add_roles(tempUser, togive, chst)
                            elif index == 6:
                                await client.add_roles(tempUser, togive, cola)
                            elif index == 7:
                                await client.add_roles(tempUser, togive, cos)
                            elif index == 8:
                                await client.add_roles(tempUser, togive, ntid)
                    index += 1

        if command.lower().strip() == "remove":
            rest = message.content.strip()[7:]
            await client.send_message(message.channel, "Sorry, this bit is under construction, bug Brandon for help!")


client.run('0')  # Your server api key thing goes here
