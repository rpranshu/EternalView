#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from sys import platform
from termcolor import colored
from urllib.request import urlopen
if platform == "linux" or platform == "linux2" or platform == "darwin":
    os.system("resize -s 27 85")
elif platform == "win32":
    os.system("mode con cols=85 lines=27")
print (colored('                 -= Built with Swag by PRANSHU RANAKOTI  ©2018 =-                     ','red',attrs=['bold']))
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
print (colored('Welcome to EternalView, the all-seeing ᒡ◯ᵔ◯ᒢ information gathering tool!', 'cyan',))
print (' ' )
def opt():
    print (' ***********',(colored('MENU','yellow',attrs=['bold'])), '***********')
    print (' *                          *')
    print (colored(" * 1. Whois information     * ",'white',attrs=['bold']))
    print (" * 2. DNS Lookup            * ")
    print (colored(" * 3. Cloudflare Detection  * ",'red', attrs=['bold']))
    print (colored(" * 4. IP Locator            * ",'magenta',attrs=['bold']))
    print (colored(" * 5. HTTP Headers          * ",'yellow',attrs=['bold']))
    print (" * 6. Robots.txt Scanner    * ")
    print (colored(" * 7. Associated links      * ",attrs=['bold']))
    print (colored(" * 8. Nmap Scan             * ",'cyan',attrs=['bold']))
    print (colored(" * 9. Trace the route       * ",'white',attrs=['bold']))
    print (colored(' * 10. HTTP DOS Test        * ','red',attrs=['bold']))
    print (colored(' * 11. Exit                 * ','yellow',attrs=['bold']))
    print (' ****************************')
opt()
def view():
    try:
        option = eval(input (' '+'\033[0;41m What would you like to do?:\033[1;m'))
        print (' ')
        if option == 1: 
            if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
                os.system('say Enter the Domain or eyepee address')
                print (os.system("whois"+' '+input('\033[1;91mDomain address or ip address:\033[1;m')))
                os.system('say task completed successfully')
            elif platform == 'win32':
                print (urlopen("http://api.hackertarget.com/whois/?q=" + ipaddr).read())
            opt()
            view()
        if option == 2:
            if platform == 'linux' or platform == 'linux2' or platform == 'darwin' :
                os.system('say Enter the Domain or eyepee address')
                print (os.system("dig" +" "+ input('\033[1;91mEnter Domain: \033[1;m')))
                os.system('say task completed successfully')
            if platform == 'win32':
                print (urlopen('http://api.hackertarget.com/dnslookup/?q=' + input('\033[1;91mEnter Domain: \033[1;m')).read())
            opt()
            view()
        if option ==3:
            os.system('say Enter the Domain or eyepee address')
            dnseval = urlopen("http://tools.bevhost.com/cgi-bin/dnslookup?data=" + input('\033[1;91mEnter Domain: \033[1;m')).read()
            if 'cloudflare' in dnseval:
                print (colored("Cloudflare Detected","green",attrs=['bold']))
                os.system('say task completed successfully')
            else:
                print (colored("Not Protected By cloudflare", "red",attrs=['bold']))
                os.system('say task completed successfully')
            opt()
            view()
        if option == 4:
            os.system('say Enter the Domain or eyepee address')
            print (os.system('curl ipinfo.io/'+input('\033[1;91mEnter IP Address: \033[1;m') + '/geo'))
            os.system('say Task completed successfully')
            opt()
            view()
        if option == 5:
            os.system('say Enter the Domain or eyepee address')
            print (os.system('curl -v '+' '+input('\033[1;91mEnter Domain or IP Address: \033[1;m')))
            os.system('say Task completed successfully')
            opt()
            view()
        if option == 6:
            os.system('say Enter the Domain address')
            ipaddr = input('\033[1;91mEnter Domain: \033[1;m')
            if 'http://' in ipaddr or 'https://' in ipaddr:
                pass
            else:
                ipaddr = 'http://' + ipaddr
            print (urlopen(ipaddr + "/robots.txt").read())
            os.system('say Task completed successfully')
            opt()
            view()
        if option == 7:
            os.system('say Enter the you are elle')
            links = input('\033[1;91mEnter URL: \033[1;m')
            if 'http://' in links or 'https://' in links:
                pass
            else:
                links = 'http://' + links 
            print (urlopen("https://api.hackertarget.com/pagelinks/?q=" + links).read())
            os.system('say Task completed successfully')
            opt()
            view()
        if option == 8:
            os.system('say Enter the Domain or eyepee address')
            print (os.system('sudo nmap -O -Pn -p 1-65535 -sS -sV'+ ' ' + input('\033[1;91mEnter Domain or IP Address: \033[1;m')))
            os.system('say Task completed successfully')
            opt()
            view()
        if option == 9:
            os.system('say Enter the Domain or eyepee address')
            print (os.system("traceroute" +' '+ input('\033[1;91mEnter Domain or IP Address: \033[1;m')))
            os.system('say Task completed successfully')
            opt()
            view()
        if option == 10:
            os.system('say Enter the Domain or eyepee address')
            print(os.system('python goldeneye.py '+input('\033[1;91mEnter Domain or IP Address: \033[1;m')+' -w 50'))
            os.system('say Task completed successfully')
            opt()
            view()
        if option == 11:
            os.system("killall Terminal")
        else:
            print (colored(' '+'██████INVALID OPTION!!██████','red','on_white',attrs=['blink']))
            opt()
            view()
    except:
        print (' ')
        print (colored(' '+'██████PLEASE ENTER A VALID VALUE!!██████','red','on_white',attrs=['blink']))
        print (' ')
        opt()
        view()
view()
