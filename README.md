# MajorMaster
A WIP Discord bot for managing roles, specifically those related to majors and colleges at RIT.

You will need to edit these source files with relevant information for proper functionality. See inline comments

#Requirements
discord 0.16.12

discord.py 0.16.12

aiohttp 1.0.5

chardet 3.0.4

mutlidict 4.5.2

pip 9.0.1

setuptools 28.8.0

websockets 3.4


Server must have the following roles: CAD, SCOB, GCCIS, KGCOE, CET, CHST, COLA, NTID, COS, UE

#Commands:

createAlltheRoles - creates all major roles. Locked to owner ID, needs manually set

add [major name here] - this is channel locked, capitalization doesn't matter, but the full name of the major must be used.