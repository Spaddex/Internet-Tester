#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""-------------IMPORTS------------"""
import time
import requests
import colorama
import subprocess
import signal
import sys
"""--------------------------------"""

forsok=0
def anslutning():
	global forsok
	try:
		global svar
		svar=requests.get("http://www.google.com")
		
	except:
		if forsok < 1:
			print ('\033[31m'+"[+]Nope, No internet, trying again in 10 seconds. \n ")
			time.sleep(10)
			forsok+=1
			anslutning()

		else:
			print('\033[31m'+"[+]Still no internet, vill retry again in 10 seconds")
			if (forsok%6)==0:
				print('[+]VWe haven\'t had internet in ' +str(forsok/6)+ " minutes =/ \n")
			time.sleep(10)
			forsok+=1
			anslutning()
	
	if svar.status_code == 200:
		print('\033[32m'+"[+]Wo-ho!")
		success()
			
def success():
	for a in range(0,5):
		print("\a We got internet!!!! :D")
		time.sleep(1)
		
	print("[+]Testing the connection, uno momento!")
	print("\033[34m")
	subprocess.Popen([r"./speedtest-cli"])
	time.sleep(150)
		
def signal_handler(signal, frame):
    print ('\n [+]And we\re done!')
    sys.exit(0)	
    
signal.signal(signal.SIGINT, signal_handler) #Sätter en signal handler som gör att ctrl+c ej skickar felmeddelande

anslutning()


