#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import threading
from datetime import datetime
import hashlib
import json
import os
import pathlib
import socket
import time
from requests import get
import requests
from sys import platform
from colorama import Fore, init, Style

if platform == "win32":
    from ctypes import wintypes

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ProjectPath = (os.path.dirname(os.path.abspath(__file__)))
corepath = ProjectPath + "/core"
sherlockpath = ProjectPath + "/core/sherlock/sherlock"
pingpath = ProjectPath + "/core/ping"
dbspath = ProjectPath + "/core/dbs/"
instagrampath = ProjectPath + "/core/instagram"
sublisterpath = ProjectPath + "/core/Sublist3r"
phonefinderpath = ProjectPath + "/core/email2phonenumber"
ghuntpath = ProjectPath + "/core/GHunt"
harvesterpath = ProjectPath + "/core/theHarvester"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


with open('config.json', 'r') as settings:
    config = json.load(settings)
    username = (config["username"])
    color = (config["color"])
    autoupdate = (config["autoupdate"])

if color == "RED":
    color = Fore.RED
elif color == "LIGHT_RED":
    color = Fore.LIGHTRED_EX
elif color == "BLUE":
    color = Fore.BLUE
elif color == "LIGHT_BLUE":
    color = Fore.LIGHTBLUE_EX
elif color == "MAGENTA":
    color = Fore.MAGENTA
elif color == "LIGHT_MAGENTA":
    color = Fore.LIGHTMAGENTA_EX
elif color == "YELLOW":
    color = Fore.YELLOW
elif color == "LIGHT_YELLOW":
    color = Fore.LIGHTYELLOW_EX
elif color == "GREEN":
    color = Fore.GREEN
elif color == "LIGHT_GREEN":
    color = Fore.LIGHTGREEN_EX
elif color == "CYAN":
    color = Fore.CYAN
elif color == "LIGHT_CYAN":
    color = Fore.LIGHTCYAN_EX
elif color == "BLACK":
    color = Fore.BLACK
else:
    color = Fore.LIGHTWHITE_EX
    print("INVALID COLOR.")

errorcolor = Fore.RED
warningcolor = Fore.LIGHTRED_EX
eventcolor = Fore.YELLOW

def error(message):
    print(f"{errorcolor}[ERROR] {Fore.LIGHTWHITE_EX}| {message}")

def warning(message):
    print(f"{warningcolor}[WARNING] {Fore.LIGHTWHITE_EX}| {message}")

def event(message):
    print(f"{eventcolor}[EVENT] {Fore.LIGHTWHITE_EX}| {message}")

def update():
    try:
        os.system("git pull")
        event("Successfully updated")
        input("Press enter to continue")
    except:
        error("Failed to update.")

version = "1.5.6"
windowsize = "95,22"

if platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Azrael - Version " + version)
    init(convert=True)
    cmd = 'mode ' + windowsize
    os.system(cmd)
    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)

    font.nFont = 12
    font.dwFontSize.X = 18
    font.dwFontSize.Y = 24
    font.FontFamily = 54
    font.FontWeight = 700
    font.FaceName = "Consolas"
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))

def load():
    event(f"{Fore.LIGHTWHITE_EX}Checking for updates...")
    if autoupdate:
        git = pathlib.Path("git")
        if git.is_dir():
            update()
    event(f"{Fore.LIGHTWHITE_EX}Loading core & modules...")
    time.sleep(0.10)
    event(f"{Fore.LIGHTWHITE_EX}Verifying integrity...")
    core = pathlib.Path("core")
    if core.is_dir():
        # this shitty little check just makes sure the directory "core" is in the main file LOOL
        event(f"{Fore.LIGHTWHITE_EX}Integrity verified.")
    else:
        time.sleep(0.10)
        error(f"{Fore.LIGHTWHITE_EX}Verification failed.")
        print("Please install the core at")
        print("https://github.com/flairings, if you are using a development version contact Flairings#0608")
        time.sleep(20)
        exit(0)
    event(f"Logged in as: {Fore.GREEN}{username}")
    if platform == "win32":
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW("Azrael - Version " + version + f" | User: {username}")

def onlaunch():
    clear()
    banner()
    load()
    ideal()


def banner():
    clear()
    if platform == "win32":
        print(f"""{Style.BRIGHT}
                        	       {color}╔{Fore.LIGHTWHITE_EX}═╗{Fore.LIGHTWHITE_EX}╔{color}═{Fore.LIGHTWHITE_EX}╗{color}╦{Fore.LIGHTWHITE_EX}═{color}╗╔═{Fore.LIGHTWHITE_EX}╗╔{color}═╗{Fore.LIGHTWHITE_EX}╦  
                        	       {color}╠═{Fore.LIGHTWHITE_EX}╣{color}╔{color}═{Fore.LIGHTWHITE_EX}╝╠{Fore.LIGHTWHITE_EX}╦{color}╝{Fore.LIGHTWHITE_EX}╠═{color}╣{Fore.LIGHTWHITE_EX}║╣ ║  
                        	       ╩ {color}╩{Fore.LIGHTWHITE_EX}╚{color}═╝{Fore.LIGHTWHITE_EX}╩╚{color}═{color}╩{Fore.LIGHTWHITE_EX} ╩{color}╚{Fore.LIGHTWHITE_EX}═{color}╝╩{Fore.LIGHTWHITE_EX}═╝ {Style.RESET_ALL}
                            {Fore.LIGHTWHITE_EX}Intelligence & Penetration interface \n""")

def ideal():
    os.chdir(ProjectPath)
    global username
    print("")
    commandline = (color + username + "@Azrael:~$ ")
    command = input(commandline)

    if command.lower().replace(" ","") == "help":
        clear()
        banner()
        print(f"{color}                       ┌────────────────────────────────────────────┐")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}IPLOOKUP {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Searches an IP for details      {color}│")
        print(f"{color}                       │ {color}RESOLVE  {Fore.WHITE}| {color}Shows the ip of a domain        {color}│")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}SHERLOCK {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Search the socials of a name    {color}│")
        print(f"{color}                       │ {color}COLOR    {Fore.WHITE}| {color}Change the color of terminal  {color}  │")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}CLS      {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Clears the screen               {color}│")
        print(f"{color}                       └────────────────────────────────────────────┘")
        print(f"{color}                                       ┌────────────┐")
        print(f"{color}                                       │  {Fore.LIGHTWHITE_EX}Page {Fore.LIGHTWHITE_EX}1/{Fore.LIGHTWHITE_EX}4{color}  │")
        print(f"{color}                                       └────────────┘")
        ideal()

    if command.lower() == "help 2":
        clear()
        banner()
        print(f"{color}                       ┌────────────────────────────────────────────┐")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}SUBLIST  {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Shows subdomains of a domain    {color}│")
        print(f"{color}                       │ {color}HASH     {Fore.WHITE}| {color}Hash a string in algorithms     {color}│")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}PORTSCAN {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Shows the ports of a host       {color}│")
        print(f"{color}                       │ {color}STEAM    {Fore.WHITE}| {color}Shows info of Steam ID          {color}│")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}IGREPORT {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Reports an instagram account    {color}│")
        print(f"{color}                       └────────────────────────────────────────────┘")
        print(f"{color}                                       ┌────────────┐")
        print(f"{color}                                       │  {Fore.LIGHTWHITE_EX}Page {Fore.LIGHTWHITE_EX}2/{Fore.LIGHTWHITE_EX}4{color}  │")
        print(f"{color}                                       └────────────┘")
        ideal()

    if command.lower() == "help 3":
        clear()
        banner()
        print(f"{color}                       ┌────────────────────────────────────────────┐")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}PING     {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Pings an ip address             {color}│")
        print(f"{color}                       │ {color}TCPPING  {Fore.WHITE}| {color}TCP pings an ip address         {color}│")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}UUID     {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Returns UUID of MC username   {color}  │")
        print(f"{color}                       │ {color}MCSERVER {Fore.WHITE}| {color}Information about a mc server {color}  │")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}DBSEARCH {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Search over 150 MC databases    {color}│")
        print(f"{color}                       └────────────────────────────────────────────┘")
        print(f"{color}                                       ┌────────────┐")
        print(f"{color}                                       │  {Fore.LIGHTWHITE_EX}Page {Fore.LIGHTWHITE_EX}3/{Fore.LIGHTWHITE_EX}4{color}  │")
        print(f"{color}                                       └────────────┘")
        ideal()

    if command.lower() == "help 4":
        clear()
        banner()
        print(f"{color}                       ┌────────────────────────────────────────────┐")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}PHONEBRUTE {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Searches for a phone number   {color}│")
        print(f"{color}                       │ {color}PORTS      {Fore.WHITE}| {color}List of all ports             {color}│")
        print(f"{color}                       │ {Fore.LIGHTWHITE_EX}GHUNT      {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Show info from Gmail Account  {color}│")
        print(f"{color}                       │ {color}HARVESTER  {Fore.WHITE}| {color}Shows subdomains, emails, ips {color}│")
        print(f"{color}                       └────────────────────────────────────────────┘")
        print(f"{color}                                       ┌────────────┐")
        print(f"{color}                                       │  {Fore.LIGHTWHITE_EX}Page {Fore.LIGHTWHITE_EX}4/{Fore.LIGHTWHITE_EX}4{color}  │")
        print(f"{color}                                       └────────────┘")
        ideal()

    if command.lower().replace(" ","") == "ports":
        print("")
        print(f"{color}  ┌──────────────────────┐")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}        PORTS {color}       │")
        print(f"{color}  ├──────────────────────┤")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}21   | SFTP {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}22   | SSH {color}          │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}23   | TELNET {color}       │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}25   | SMTP {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}53   | DNS {color}          │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}69   | TFTP {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}80   | HTTP {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}443  | HTTPS {color}        │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}3074 | XBOX {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}9307 | PLAYSTATION {color}  │")
        print(f"{color}  └──────────────────────┘")
        ideal()

    if command.lower().replace(" ","") == "iplookup":
        ip = str(input("ip: "))
        pr = requests.post('http://ip-api.com/json/' + ip)
        if '"status":"success"' in pr.text:
            print("")
            print(f"┌────────────────────────────────────")
            print(f"│       {Fore.LIGHTWHITE_EX}IPLOOKUP {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{ip}         {color}")
            print(f"├────────────────────────────────────")
            print(f"│ {Fore.LIGHTWHITE_EX}Country {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['country']} {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}Country Code {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['countryCode']} {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}Region Name {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['regionName']} {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}City {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['city']}  {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}Timezone {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['timezone']}   {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}Zip {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['zip']}   {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}ISP {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['isp']}  {color}")
            print(f"└───────────────────────────────────")
        else:
            warning(f"{Fore.LIGHTRED_EX} IP Address could not be found.")
        ideal()

    if command.lower().replace(" ","") == "resolve":
        hostname = str(input("domain: "))
        try:
            ip = socket.gethostbyname(hostname)
            pr = requests.post('http://ip-api.com/json/' + ip)
            if '"status":"success"' in pr.text:
                print("")
                print(f"┌──────────────────────────────────────")
                print(f"│    {Fore.LIGHTWHITE_EX}RESOLVE {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{hostname}{color}")
                print(f"├──────────────────────────────────────")
                print(f"│ {Fore.LIGHTWHITE_EX}{hostname} {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{ip}{color}")
                print(f"│ {Fore.LIGHTWHITE_EX}Country {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['country']} {color}")
                print(f"│ {Fore.LIGHTWHITE_EX}Country Code {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['countryCode']} {color}")
                print(f"│ {Fore.LIGHTWHITE_EX}Region Name {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['regionName']} {color}")
                print(f"│ {Fore.LIGHTWHITE_EX}City {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['city']}  {color}")
                print(f"│ {Fore.LIGHTWHITE_EX}Timezone {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['timezone']}   {color}")
                print(f"│ {Fore.LIGHTWHITE_EX}Zip {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['zip']}   {color}")
                print(f"│ {Fore.LIGHTWHITE_EX}ISP {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{pr.json()['isp']}  {color}")
                print(f"└───────────────────────────────────")
        except socket.gaierror:
            warning(f"{Fore.LIGHTRED_EX} Domain could not be found.")
        ideal()

    if command.lower().replace(" ","") == "sherlock":
        sherlockusername = str(input("username: "))
        if " " in username:
            error("username must only contain single string.")
            ideal()
        try:
            os.chdir(sherlockpath)
            print("")
            event("Searching for " + sherlockusername)
            print("")
            os.system("python sherlock.py " + sherlockusername)
            event("Process complete")
        except:
            error("unknown error occurred")
        ideal()

    if command.lower().replace(" ","") == "sublist":
        domain = str(input("Domain: "))
        os.chdir(sublisterpath)
        print(Fore.LIGHTWHITE_EX)
        os.system("python Sublist3r.py -d " + domain)
        event("Process complete")
        ideal()

    if command.lower().replace(" ","") == "tcpping":
        ip = str(input("IP: "))
        if " " in ip:
            error("IP variable must only contain single string.")
            ideal()
        port = str(input("Port: "))
        if " " in port:
            error("Port variable must only contain single string.")
            ideal()
        amount = str(input("attempts to ping (0=infinite): "))
        if amount == "0":
            amount = "5000"
        if " " in amount:
            error("Amount variable must only contain single int.")
            ideal()
        try:
            os.chdir(pingpath)
            print("")
            event("Pinging " + ip)
            print("")
            os.system("paping.exe -c " + amount + " -p " + port + " " + ip)
            event("Process complete")
        except:
            error("unknown error occurred")
        ideal()

    if command.lower().replace(" ","") == "ping":
        print("")
        warning("Once pinging you cannot return back to Azrael.")
        time.sleep(3)
        os.chdir(pingpath)
        os.system('cmd /c "pinger.bat')
        event("Process complete")
        ideal()

    if command.lower().replace(" ","") == "mcserver":
        domain = str(input("Domain: "))
        req = requests.get(f'https://api.mcsrvstat.us/2/{domain}')
        if 'online":true' in req.text:
            pr = requests.post('http://ip-api.com/json/' + req.json()['ip'])
            print("")
            print(f"{color}┌────────────────────────────────────")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}MC Server Information {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{domain}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}IP: {req.json()['ip']}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}ISP: {Fore.LIGHTWHITE_EX}{pr.json()['isp']} ")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}Port: {req.json()['port']}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}Version: {req.json()['version']}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}Players: {req.json()['players']['online']}/{req.json()['players']['max']}")
            print(f"{color}└───────────────────────────────────")
        else:
            print("")
            error("Invalid domain or service is offline.")
        ideal()

    if command.lower().replace(" ","") == "uuid":
        names = []
        names.clear()
        mcUser = input("Username: ")
        req = requests.get(f'https://playerdb.co/api/player/minecraft/{mcUser}')
        if 'code":"player.found"' in req.text:
            try:
                print("")
                print(f"{color}┌────────────────────────────────────")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}{mcUser} {Fore.WHITE}| {Fore.LIGHTWHITE_EX}UUID Information")
                print(f"{color}├────────────────────────────────────")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}Full UUID: {req.json()['data']['player']['id']}")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}Trimmed UUID: {req.json()['data']['player']['raw_id']}")
                for name in req.json()['data']['player']['meta']['name_history']:
                    names.append(name['name'])
                print(f"{color}│ {Fore.LIGHTWHITE_EX}Passed Usernames ({len(names)}): {names}")
                print(f"{color}└───────────────────────────────────")
                ideal()
            except Exception as e:
                error(e)
                ideal()
        else:
            event("Invalid username or ID.")
            ideal()

    if command.lower().replace(" ","") == "steam":
        names = []
        names.clear()
        steamID = input("ID: ")
        req = requests.get(f'https://playerdb.co/api/player/steam/{steamID}')
        if 'code":"player.found"' in req.text:
            try:
                print("")
                print(f"{color}┌────────────────────────────────────")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}{steamID} {Fore.WHITE}| {Fore.LIGHTWHITE_EX}ID Information")
                print(f"{color}├────────────────────────────────────")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}Username: {req.json()['data']['player']['username']}")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}Real name: {req.json()['data']['player']['meta']['realname']}")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}Personaname: {req.json()['data']['player']['meta']['personaname']}")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}Avatar URL: {req.json()['data']['player']['avatar']}")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}Country: {req.json()['data']['player']['meta']['loccountrycode']}")
                print(f"{color}│ {Fore.LIGHTWHITE_EX}State: {req.json()['data']['player']['meta']['locstatecode']}")
                print(f"{color}└───────────────────────────────────")
                ideal()
            except Exception as e:
               # error(e)
                pass
                ideal()
        else:
            event("Invalid ID.")
            ideal()

    if command.lower().replace(" ","") == "dbsearch":
        dbs = pathlib.Path("core/dbs")
        if not dbs.is_dir():
            error("You must install the databases to use this module")
            print("You can download the databases at https://flairings.agency/projects/azrael")
            input()
            exit(0)
        search_str = input("Search: ")
        if platform == "win32":
            command = 'mode 150,18'
            os.system(command)
        event("Beginning search.")
        if not (dbspath.endswith("/") or dbspath.endswith("\\")):
            search_path = dbspath + "/"
            print(search_path)
        if not os.path.exists(dbspath):
            search_path = "."
            print(search_path)
        for fname in os.listdir(path=dbspath):
            if fname.endswith("txt"):
                fo = open(dbspath + fname, errors='ignore')
                line = fo.readline()
                line_no = 1
                while line != '':
                    index = line.find(search_str)
                    if index != -1:
                        print(Fore.LIGHTBLUE_EX + fname + Fore.WHITE + " | ", color + line, sep="")
                    line = fo.readline()
                    line_no += 1
                fo.close()
        print("")
        event(Fore.LIGHTWHITE_EX + "Process complete")
        if platform == "win32":
            input("Press enter to return to default terminal size and commandline mode.")
            command = 'mode ' + windowsize
            os.system(command)
        banner()
        ideal()

    if command.lower().replace(" ","") == "igreport":
        os.chdir(instagrampath)
        print(Fore.LIGHTWHITE_EX)
        os.system('cmd /c "python instaspamv4.py ')
        print("")
        event(Fore.LIGHTWHITE_EX + "Process complete")
        ideal()

    if command.lower().replace(" ","") == "hash":
        hash_str = input("string: ")
        try:
            command = 'mode 150,18'
            os.system(command)
            sha224 = hashlib.sha224(f"{hash_str}".encode()).hexdigest()
            sha256 = hashlib.sha256(f"{hash_str}".encode()).hexdigest()
            sha384 = hashlib.sha384(f"{hash_str}".encode()).hexdigest()
            sha512 = hashlib.sha512(f"{hash_str}".encode()).hexdigest()
            md5 = hashlib.md5(f"{hash_str}".encode()).hexdigest()
            shake_128 = hashlib.shake_128(f"{hash_str}".encode()).hexdigest(12)
            shake_256 = hashlib.shake_256(f"{hash_str}".encode()).hexdigest(12)
            print("")
            print(f"{color}┌────────────────────────────────────")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}{hash_str} {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Successfully hashed")
            print(f"{color}├────────────────────────────────────")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}sha224: {sha224}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}sha256: {sha256}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}sha384: {sha384}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}sha512: {sha512}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}md5: {md5}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}shake_128: {shake_128}")
            print(f"{color}│ {Fore.LIGHTWHITE_EX}shake_256: {shake_256}")
            print(f"{color}└───────────────────────────────────")
            if platform == "win32":
                input("Press enter to return to default terminal size and commandline mode.")
                command = 'mode ' + windowsize
                os.system(command)
        except error as e:
            error(e)
        banner()
        ideal()

    def TCP_connect(ip, port_number, delay, output):
        TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        TCPsock.settimeout(delay)
        try:
            TCPsock.connect((ip, port_number))
            output[port_number] = 'Listening'
        except:
            output[port_number] = ''

    def scan_ports(host_ip, delay):

        threads = []  # To run TCP_connect concurrently
        output = {}  # For printing purposes

        # Spawning threads to scan ports
        for i in range(10000):
            t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
            threads.append(t)

        # Starting threads
        for i in range(10000):
            threads[i].start()

        # Locking the main thread until all threads complete
        for i in range(10000):
            threads[i].join()

        # Printing listening ports from small to large
        for i in range(10000):
            if output[i] == 'Open':
                print(str(i) + ': ' + output[i])

    if command.lower().replace(" ","") == "portscan":
        host = input("host: ")
        event(Fore.LIGHTWHITE_EX + "Scanning ports... ")
        os.system(f"nmap -F {host}")
        event(Fore.LIGHTWHITE_EX + "Process complete")
        ideal()

    if command.lower().replace(" ","") == "phonebrute":
        email = input("email: ")
        os.chdir(phonefinderpath)
        time.sleep(0.500)
        print("")
        event(Fore.LIGHTWHITE_EX + f"Beginning phone brute force {Style.RESET_ALL}")
        print("")
        os.system(f"python email2phonenumber.py scrape -e {email}")
        print("")
        event(Fore.LIGHTWHITE_EX + "Process complete")
        ideal()

    if command.lower().replace(" ","") == "ghunt":
        email = input("gmail: ")
        os.chdir(ghuntpath)
        time.sleep(0.500)
        print("")
        event(Fore.LIGHTWHITE_EX + f"Beginning google account hunter {Style.RESET_ALL}")
        print("")
        os.system(f"python ghunt.py email {email}")
        print("")
        event(Fore.LIGHTWHITE_EX + "Process complete")
        ideal()

    if command.lower().replace(" ","") == "nmap":
        host = input("host: ")
        time.sleep(0.500)
        print("")
        event(Fore.LIGHTWHITE_EX + f"Beginning nmap type intense {Style.RESET_ALL}")
        print("")
        os.system(f"nmap -T4 -A -v {host}")
        print("")
        event(Fore.LIGHTWHITE_EX + "Process complete")
        ideal()

    if command.lower().replace(" ","") == "harvester":
        host = input("host: ")
        os.chdir(harvesterpath)
        time.sleep(0.500)
        print("")
        event(Fore.LIGHTWHITE_EX + f"Beginning harvester {Style.RESET_ALL}")
        os.system(f"python theHarvester.py -d {host} -b google")
        print("")
        event(Fore.LIGHTWHITE_EX + "Process complete")
        ideal()

    def restart():
        os.chdir(ProjectPath)
        os.system("python Azrael.py")

    if command.lower().replace(" ","") == "color":
        print("")
        print(f"{Fore.LIGHTWHITE_EX}Available colors for the terminal:")
        print(f"{Fore.WHITE}> {Fore.RED}RED")
        print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}LIGHT_RED")
        print(f"{Fore.WHITE}> {Fore.BLUE}BLUE")
        print(f"{Fore.WHITE}> {Fore.LIGHTBLUE_EX}LIGHT_BLUE")
        print(f"{Fore.WHITE}> {Fore.MAGENTA}MAGENTA")
        print(f"{Fore.WHITE}> {Fore.LIGHTMAGENTA_EX}LIGHT_MAGENTA")
        print(f"{Fore.WHITE}> {Fore.YELLOW}YELLOW")
        print(f"{Fore.WHITE}> {Fore.LIGHTYELLOW_EX}LIGHT_YELLOW")
        print(f"{Fore.WHITE}> {Fore.GREEN}GREEN")
        print(f"{Fore.WHITE}> {Fore.LIGHTGREEN_EX}LIGHT_GREEN")
        print(f"{Fore.WHITE}> {Fore.CYAN}CYAN")
        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}LIGHT_CYAN")
        print(f"{Fore.WHITE}> {Fore.WHITE}BLACK (example white as black does not show on terminal)")
        print("")
        os.chdir(ProjectPath)
        newcolor = input(f"{Fore.LIGHTWHITE_EX}Select a new color for the terminal: ")
        with open("config.json", 'r') as f:
            colorconfigloader = json.load(f)
        colorconfigloader[str("color")] = newcolor
        with open("config.json", 'w') as f:
            json.dump(colorconfigloader, f, indent=4)
        print(f"{color}color has been set to " + newcolor)
        print(f"Azrael will restart in {Fore.WHITE}3 {color}seconds")
        time.sleep(3)
        restart()

    if command.lower().replace(" ","") == "cls":
        banner()
        ideal()

    if command.lower().replace(" ","") == "update":
        update()
        banner()
        ideal()

    if command.lower().replace(" ","") == "home":
        clear()
        banner()
        load()
        ideal()

    else:
        print("")
        error(f"{Fore.LIGHTWHITE_EX}Unknown command, type 'help' for a list of commands.")
        warning(f"{Fore.LIGHTWHITE_EX}All commands must be lowercase.")
        ideal()


# Start Azrael
onlaunch()
