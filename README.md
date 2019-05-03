# MajorMaster
A WIP Discord bot for managing roles, specifically those related to majors and colleges at RIT.

You will need to edit these source files with relevant information for proper functionality. See inline comments

##Requirements
discord 1.0.1

discord.py 1.0.1

aiohttp 3.5.4

async-timeout 3.0.1

attrs 19.1.0

idna 2.8

chardet 3.0.4

mutlidict 4.5.2

pip 10.0.1

setuptools 39.1.0

websockets 6.0

yarl 1.3.0


Server must have the following roles: CAD, SCOB, GCCIS, KGCOE, CET, CHST, COLA, NTID, COS, UE

##Commands:

createAlltheRoles - creates all major roles. Locked to owner ID, needs manually set. caps matter only for this command

add [role here] - this is channel locked, capitalization doesn't matter, but the full name of the major must be used.
this will add the related college if applicable

remove [role here] - channel locked, removes a role

help - displays help

roles - displays all the roles

