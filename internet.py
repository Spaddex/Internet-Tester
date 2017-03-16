#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""-------------IMPORTS------------"""
import time
import requests
import subprocess
import signal
import sys

"""--------------------------------"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

forsok = 0


def anslutning():
    global forsok
    try:
        global svar
        svar = requests.get("http://www.google.com")

    except:
        if forsok < 1:
            print(bcolors.FAIL + "[+] Nope, no internet, trying again in 10 seconds. \n ")
            time.sleep(10)
            forsok += 1
            anslutning()

        else:
            print(bcolors.FAIL + "[+] Still no internet. Will retry again in 10 seconds")
            if (forsok % 6) == 0:
                print('[+] We haven\'t had internet in ' + str(forsok / 6) + " minutes =/ \n")
            time.sleep(10)
            forsok += 1
            anslutning()

    if svar.status_code == 200:
        print(bcolors.OKGREEN + "[+] Wo-ho!")
        success()


def success():
    for a in range(0, 5):
        print( bcolors.OKGREEN + "\a We got internet!!!! :D")
        time.sleep(1)

    print( bcolors.OKGREEN + "[+] Testing the connection, uno momento!")
    print("\033[34m")
    subprocess.Popen([r"./speedtest-cli"])
    time.sleep(150)


def signal_handler(signal, frame):
    print(bcolors.OKBLUE + "\n [+] And we're done!")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)  # Sätter en signal handler som gör att ctrl+c ej skickar felmeddelande

anslutning()
