#!/usr/bin/env python
'''
1. Make sure to update your python3 framework before running
2. Make sure you have NMAP installed
3. Make sure you have the latest metasploit framework installed
4. Make sure you have necessary permissions from the web-admin/sysadmin to perform different tests
5. Make sure to use some common sense!
'''
# -*- coding: utf-8 -*-
import os
import subprocess
from sys import platform
from termcolor import colored
from urllib.request import urlopen
os.system("resize -s 29 85") #Resize the window (looks cool!)
print (colored('                 -= Built with <3 by PRANSHU RANAKOTI  ©2018 =-                     ','red',attrs=['bold']))
def eternal():
    print (colored('   ▄████████     ███        ▄████████    ▄████████ ███▄▄▄▄      ▄████████   ▄█      ' , 'red'))
    print (colored('  ███    ███ ▀█████████▄   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███  ███      ' , 'red'))
    print (colored('  ███    █▀     ▀███▀▀██   ███    █▀    ███    ███ ███   ███   ███    ███  ███      ' , 'red'))
    print (colored(' ▄███▄▄▄         ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███   ███   ███    ███  ███      ' , 'red'))
    print (colored('▀▀███▀▀▀         ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███   ███ ▀███████████  ███      ' , 'red'))
    print (colored('  ███    █▄      ███       ███    █▄  ▀███████████ ███   ███   ███    ███  ███      ' , 'red'))
    print (colored('  ███    ███     ███       ███    ███   ███    ███ ███   ███   ███    ███  ███▌    ▄' , 'red'))
    print (colored('  ██████████    ▄████▀     ██████████   ███    ███  ▀█   █▀    ███    █▀   █████▄▄██' , 'red'))
eternal()
print (' ')
print (colored('      Welcome to EternalView™, the all-seeing ᒡ◯ᵔ◯ᒢ information gathering tool!', 'cyan',))
print (' ')
def opt():
    print (colored(' ***********','green',attrs=['bold']),(colored('MENU','yellow',attrs=['bold'])), colored('***********','green',attrs=['bold']))
    print (colored(" * 1. Whois information     * ",'green',attrs=['bold']))
    print (colored(" * 2. DNS Lookup            * ",'cyan',attrs=['bold']))
    print (colored(" * 3. Cloudflare Detection  * ",'red', attrs=['bold']))
    print (colored(" * 4. IP Locator            * ",'magenta',attrs=['bold']))
    print (colored(" * 5. HTTP Headers          * ",'yellow',attrs=['bold']))
    print (colored(" * 6. Robots.txt Scanner    * ",'green',attrs=['bold']))
    print (colored(" * 7. Associated links      * ",'cyan',attrs=['bold']))
    print (colored(" * 8. Nmap Scan             * ",'yellow',attrs=['bold']))
    print (colored(" * 9. Trace the route       * ",'magenta',attrs=['bold']))
    print (colored(' * 10. HTTP DOS Test        * ','green',attrs=['bold']))
    print (colored(' * 11. Autopwn™             * ','cyan',attrs=['bold']))
    print (colored(' * 12. Reload               * ','green',attrs=['bold']))
    print (colored(' * 13. Exit                 * ','red',attrs=['bold']))
    print (colored(' **************************** ','red',attrs=['bold']))
opt()
def Cerror():
	os.system("clear")
	print(" ")
	print(" ")
	print(" ")
	print(" ")
	print(" ")
	print("                             *-ERROR-*- no response from HOST!")
	print("                             Seems like Cloudflare has modified") 
	print("                             their anti-bot protection page. So")
	print("                             far it has changed maybe once per") 
	print("                             year on an average. If you notice")
	print("                             that the anti-bot page has changed,") 
	print("                             or if this module suddenly stops ") 
	print("                              working, please create a GitHub ")
	print("                             issue so that I can update the code.")
	print("                             In your issue, please include:")
	print("                             1. The full exception and stack trace.")
	print("                             2. The URL of the Cloudflare-protected ")
	print("                             page which the script does not work on.")
	print("                             3. A Pastebin or Gist containing the HTML") 
	print("                             source of the protected page.")
	os.system("tput smso; tput cup 21 29; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
	input("                             ")
	os.system("resize -s 24 85")
	eternal()
	opt()
	view()
def view():
    try:
        option = eval(input (' '+'\033[0;41m What would you like to do?:\033[1;m'+ ' '))
        print (' ')
        if option == 1:
            print (os.system("whois"+' '+input('\033[1;91mDomain address or ip address:\033[1;m')))
            opt()
            view()
        if option == 2:
            print (os.system("dig" +" "+ input('\033[1;91mEnter Domain: \033[1;m')))
            os.system("tput smso; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
            input(" ")
            os.system("resize -s 24 85")
            eternal()
            opt()
            view()
        if option ==3:
            try:
            	dnseval = urlopen("http://tools.bevhost.com/cgi-bin/dnslookup?data=" + input('\033[1;91mEnter Domain: \033[1;m')).read()
            	if 'cloudflare' in dnseval:
            		print (colored("Cloudflare Detected","green",attrs=['bold']))
            	else:
            		print (colored("Not Protected By cloudflare", "red",attrs=['bold']))
            		input(" ")
            		os.system("resize -s 24 85")
            		eternal()
            		opt()
            		view()
            except:
            	Cerror()
        if option == 4:
            print (os.system('curl ipinfo.io/'+input('\033[1;91mEnter IP Address: \033[1;m') + '/geo')) #Geoloc api ipinfo.io
            os.system("tput smso; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
            input(" ")
            os.system("resize -s 24 85")
            eternal()
            opt()
            view()
        if option == 5:
            print (os.system('curl -v '+' '+input('\033[1;91mEnter Domain or IP Address: \033[1;m')))
            os.system("tput smso; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
            input(" ")
            os.system("resize -s 24 85")
            eternal()
            opt()
            view()
        if option == 6:
            ipaddr = input('\033[1;91mEnter Domain: \033[1;m')
            if 'http://' in ipaddr or 'https://' in ipaddr:
                pass
            else:
                ipaddr = 'http://' + ipaddr
            print (urlopen(ipaddr + "/robots.txt").read())
            os.system("tput smso; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
            input(" ")
            os.system("resize -s 24 85")
            eternal()
            opt()
            view()
        if option == 7:
        	print (os.system("curl https://api.hackertarget.com/pagelinks/?q=" + input('\033[1;91mEnter the URL: \033[1;m')))
        	os.system("tput smso; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
        	input(" ")
        	os.system("resize -s 24 85")
        	eternal()
        	opt()
        	view()
        if option == 8:
            print (os.system('sudo nmap -O -sS -sV'+ ' ' + input('\033[1;91mEnter Domain or IP Address: \033[1;m')))
            os.system("tput smso; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
            input(" ")
            os.system("resize -s 24 85")
            eternal()
            opt()
            view()
        if option == 9:
            print (os.system("traceroute" +' '+ input('\033[1;91mEnter Domain or IP Address: \033[1;m')))
            os.system("tput smso; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
            input(" ")
            os.system("resize -s 24 85")
            eternal()
            opt()
            view()
        if option == 10:
            print(os.system('python goldeneye.py '+'http://'+input('\033[1;91mEnter a http domain(do not include http://): \033[1;m')+' -w 50'))
            os.system("tput smso; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
            input(" ")
            os.system("resize -s 24 85")
            eternal()
            opt()
            view()
        if option == 11:
            try:
            	os.system("chmod +x Autopwn")
            	os.system('./Autopwn')
            	os.system("tput smso; tput setaf 9;tput bold; echo Enter 'ok' to continue;tput sgr0")
            	input(" ")
            	os.system("resize -s 24 85")
            	eternal()
            	opt()
            	view()
            except:
            	printf("Autopwn™ not found, download Autopwn™ from https://github.com/rpranshu/Autopwn/releases/tag/2")
            	os.system("resize -s 24 85")
            	eternal()
            	opt()
            	view()
        if option == 12:
            os.system("python3 eternalview.py")
        if option == 13:
            os.system("killall Terminal")
        else:
            print (colored(' '+'██████INVALID OPTION!!██████','red','on_white',attrs=['blink']))
            os.system("resize -s 24 85")
            eternal()
            opt()
            view()
    except:
        print(' ')
        print(colored(' '+'██████PLEASE ENTER A VALID VALUE!!██████','red','on_white',attrs=['blink']))
        print(' ')
        os.system("killall Terminal")
view()
