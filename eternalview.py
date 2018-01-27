#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from termcolor import colored
from urllib2 import *

def eternal():
	print colored('   ▄████████     ███        ▄████████    ▄████████ ███▄▄▄▄      ▄████████   ▄█       ' , 'red')
	print colored('  ███    ███ ▀█████████▄   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███  ███       ' , 'red')
	print colored('  ███    █▀     ▀███▀▀██   ███    █▀    ███    ███ ███   ███   ███    ███  ███       ' , 'red')
	print colored(' ▄███▄▄▄         ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███   ███   ███    ███  ███       ' , 'red')
	print colored('▀▀███▀▀▀         ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███   ███ ▀███████████  ███       ' , 'red')
	print colored('  ███    █▄      ███       ███    █▄  ▀███████████ ███   ███   ███    ███  ███       ' , 'red')
	print colored('  ███    ███     ███       ███    ███   ███    ███ ███   ███   ███    ███  ███▌    ▄ ' , 'red')
	print colored('  ██████████    ▄████▀     ██████████   ███    ███  ▀█   █▀    ███    █▀   █████▄▄██ ' , 'red')
	
print colored('Welcome to Illuminati, the all-seeing ᒡ◯ᵔ◯ᒢ information gathering tool!', 'cyan',)
print (' ')
print colored('Ideal window size = 97 x 29','white')
print (' ')
print colored('-=A basic tool=-','yellow',attrs=['bold'])
print (' ')
illuminati()
def opt():
	print ' ************MENU************'
	print ' *                          *'
	print colored(" * 1. Whois information     * ",'white',attrs=['bold'])
	print " * 2. DNS Lookup            * "
	print colored(" * 3. Cloudflare Detection  * ",'cyan', attrs=['bold'])
	print colored(" * 4. IP Locator            * ",'magenta',attrs=['bold'])
	print colored(" * 5. HTTP Headers          * ",'yellow',attrs=['bold'])
	print " * 6. Robots.txt Scanner    * "
	print colored(" * 7. Associated links      * ",attrs=['bold'])
	print colored(" * 8. Nmap Scan             * ",'red',attrs=['bold'])
	print colored(" * 9. Trace the route       * ",'white',attrs=['bold'])
	print ' *                          *'
	print ' ****************************'
	#print "10. Attacks"
opt()
def eye():
	choice = input (' '+'\033[0;41m What would you like to do?:\033[1;m ')
	print ' '
        if choice == 1:
            ipaddr = raw_input('\033[1;91mDomain address or ip address: \033[1;m')
            whois = "whois"+' '+ipaddr
            evalwho = os.system(whois)
            print (evalwho)
            opt()
            eye()
        if choice == 2:
            site = raw_input('\033[1;91mEnter Domain: \033[1;m') 
            ns = "dig" +" "+ site
            dnseval = os.system(ns)
            print (dnseval)
            opt()
            eye()
        if choice ==3:
        	site = raw_input('\033[1;91mEnter Domain: \033[1;m') 
        	dns = "http://tools.bevhost.com/cgi-bin/dnslookup?data=" + site
        	dnseval = urlopen(dns).read()
        	if 'cloudflare' in dnseval:
        		print colored("Cloudflare Detected","green",attrs=['bold'])
        	else:
        		print colored("Not Protected By cloudflare", "red")
        	opt()
        	eye()
        if choice == 4:
         	ipaddr = raw_input('\033[1;91mEnter IP Address: \033[1;m')
         	loc = 'curl ipinfo.io/'+ipaddr + '/geo'
         	geoloc = os.system(loc)
         	print (geoloc)
         	opt()
         	eye()
        if choice == 5:
            ipaddr = raw_input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            ipheader = 'curl -v '+' '+ipaddr
            headereval = os.system(ipheader)
            print (headereval)
            opt()
            eye()
        if choice == 6:
            ipaddr = raw_input('\033[1;91mEnter Domain: \033[1;m')
            if 'http://' in ipaddr or 'https://' in ipaddr:
                pass
            else:
                ipaddr = 'http://' + ipaddr
            crawl = ipaddr + "/robots.txt"
            whocrawl = urlopen(crawl).read()
            print (whocrawl)
            opt()
            eye()
        if choice == 7:
            links = raw_input('\033[1;91mEnter URL: \033[1;m')
            if 'http://' in links or 'https://' in links:
                pass
            else:
                links = 'http://' + links
            associated = "https://api.hackertarget.com/pagelinks/?q=" + links
            evalassociated = urlopen(associated).read()
            print (evalassociated)
            opt()
            eye()
        if choice == 8:
        	ipaddr = raw_input('\033[1;91mEnter Domain or IP Address: \033[1;m')
        	nmap = 'sudo nmap -O -Pn -p 1-65535 -sS -sV'+ ' ' + ipaddr
        	evalnmap = os.system(nmap)
        	print (evalnmap)
        	opt()
        	eye()
        if choice == 9:
            ipaddr = raw_input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            track = "traceroute" +' '+ ipaddr
            trackeval = os.system(track)
            print (trackeval)
            opt()
            eye()
        else:
        	print colored(' '+'██████INVALID OPTION!!██████','red','on_white',attrs=['blink'])
        	opt()
        	eye()
eye()
