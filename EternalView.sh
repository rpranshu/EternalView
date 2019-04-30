#!/bin/bash
resize -s 28 88 > /dev/null 2>&1;
clear
banner(){
	tput setaf 208; tput bold
	echo -n '                      ';
	echo '-= Built with <3 by PRANSHU RANAKOTI  ©2018 =-' ;
	tput setaf 48;
	echo $'\n███████╗████████╗███████╗██████╗ ███╗   ██╗ █████╗ ██╗    ██╗   ██╗██╗███████╗██╗    ██╗\n██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔══██╗██║    ██║   ██║██║██╔════╝██║    ██║\n█████╗     ██║   █████╗  ██████╔╝██╔██╗ ██║███████║██║    ██║   ██║██║█████╗  ██║ █╗ ██║\n██╔══╝     ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║    ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║\n███████╗   ██║   ███████╗██║  ██║██║ ╚████║██║  ██║███████╗╚████╔╝ ██║███████╗╚███╔███╔╝\n╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝\n';
	tput sgr0;
	tput setaf 50;
	echo -en '          ';
	echo $'Welcome to EternalView™, the all-seeing ᒡ◯ᵔ◯ᒢ information gathering tool!\n' ;
	tput setaf 50;echo -en '**************';
	tput setaf 48;echo -en 'MENU';
	tput setaf 50;echo '***************';
	tput setaf 50;echo -en '*';tput setaf 154;             echo -en '  1. Whois information       ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 197;echo -en '  2. DNS Lookup              ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 3;  echo -en '  3. Web Technology Detection';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 51; echo -en '  4. IP Locator              ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 33; echo -en '  5. NMAP                    ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 208;echo -en '  6. Cloudflare detection    ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 118;echo -en '  7. Robots.txt enumeration  ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 248;echo -en '  8. WAF/IDS/IPS detection   ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 105;echo -en '  9. Extract HREF            ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 10; echo -en ' 10. HTTP Header             ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 9;  echo -en ' 11. Traceroute              ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 11; echo -en ' 12. AutoPwn™                ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 12; echo -en ' 13. Reload                  ';
	tput setaf 50;echo '  *';echo -en '*';tput setaf 1;  echo -en ' 14. exit                    ';
	tput setaf 50;echo -en '  *';echo $'\n*********************************';
	tput setaf 50;echo -en "What would you like to do? ";
	tput sgr0;
}
banner
tput setaf 50;
read opt;
 if [[ opt -eq '1' ]]; # WHOIS
 then tput setaf 154;
echo -en "Enter the website or IP address: ";
read site;
whois $site;
tput smso;
tput blink;
tput setaf 1;
tput bold;
echo "Press any key to continue";
tput sgr0;
read key;
clear
./EternalView.sh;
elif [[ opt -eq '2' ]]; # DNS LOOKUP
then tput setaf 197;
echo -en "Enter the website or IP address: ";
tput setaf 50;
read site;
tput sgr0;
dig  $site;
tput smso;
 tput blink;
tput setaf 1;
tput bold;
echo "Press any key to continue";
tput sgr0;
read key;
clear
./EternalView.sh;
 elif [[ opt -eq '3' ]]; #WEB TECHNOLOGY DETECTION
 then tput setaf 3;
echo -en "Enter the website or IP address: ";
read site;
wget -q https://builtwith.com/$site -O log.html;
echo "    The output has been saved as 'log.html' at";
 pwd;
echo "    Please open the file log.html in your web browser to view the results!";
tput smso;
 tput blink;
tput setaf 1;
tput bold;
echo "    Press any key to continue";
tput sgr0;
read key;
clear
./EternalView.sh;
 elif [[ opt -eq '4' ]]; # IP LOCATOR
 then tput setaf 51;
echo -en "Enter the IP address: ";
read ip;
curl ipinfo.io/$ip;
tput smso;
 tput blink;
tput setaf 1;
tput bold;
echo "Press any key to continue";
tput sgr0;
read key;
clear
./EternalView.sh;
 elif [[ opt -eq '5' ]]; #NMAP
 then tput setaf 33;
echo -en "Press 1 for basic scan and 2 for extensive scan: ";
read scan;
 	if [[ scan -eq "1" ]];
 	then echo -en "Enter the website or the IP address: ";
	read site;
	nmap $site;
	tput smso;
 	tput blink;
	tput setaf 1;
	tput bold;
	echo "If the Host is down or blocking the ping probes, try the extensive scan(option 2). Press any key to continue";
	tput sgr0;
	read key;
	clear
	./EternalView.sh;
 	elif [[ scan -eq "2" ]];
 	then echo -en "Enter the website or the IP address: ";
	read site;
	echo "THIS SCAN WILL TAKE SOME TIME, SIT BACK AND RELAX!";
	sudo nmap -sS -sV -vv --top-ports 1000 -T4 -O $site;
	tput smso;
 	tput blink;
	tput setaf 1;
	tput bold;
	echo "Press any key to continue";
	tput sgr0;
	read key;
	clear
	./EternalView.sh
	else
	tput smso;
	tput blink;
	tput setaf 1;
	tput bold;
	echo "Please choose a valid option! Press Enter to continue";
	tput sgr0;
	read key;
	clear
	./EternalView.sh 
 	fi;
elif [[ opt -eq '6' ]]; #CLOUDFLARE DETECTION
then tput setaf 208;
echo -en "Enter the website or the IP address: ";
read site;
a=$(dig $site | grep -E 'cloudflare|103.21|103.22|104.16|104|103.3|104.1|108.162.|131.0|141.101|162.15|172.6|173.245|188.114|190.93.|197.234.|198.41')
ip=$(ping -c1 $site | grep -Eo '[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9][0-9]' | head -1)
if [[ $? -eq 0 ]]; then
	echo "Runs on CF"
	echo "the IP is $ip"
else
	echo "Does not run on CF"
fi
tput smso;
tput blink;
tput setaf 1;
tput bold;
echo "Press any key to continue";
tput sgr0;
read key;
clear
./EternalView.sh;
elif [[ opt -eq '7' ]]; # ROBOTS.TXT ENUMERATION
then tput setaf 118;
echo -en "Enter the website address (DNS only): ";
read site;
robo="/robots.txt";
curl $site$robo;
tput smso;
 tput blink;
tput setaf 1;
tput bold;
echo "Press any key to continue";
tput sgr0;
read key;
clear
./EternalView.sh;
elif [[ opt -eq '8' ]]; # WAF/IDS/IPS DETECTION 
then tput setaf 190;
echo -en "Enter the website or IP address: ";
read site;
nmap -p80 --script http-waf-detect $site | grep "waf" ;
echo "Payload used : <script>alert(document.cookie)</script>";
tput smso;
tput blink;
tput setaf 1;
tput bold;
echo $'\nPress any key to continue';
tput sgr0;
read key;
clear
./EternalView.sh;
 elif [[ opt -eq '9' ]]; # EXTRACT HREF
 then tput setaf 7;
echo -en "Enter the website or IP address: ";
read site;
curl https://api.hackertarget.com/pagelinks/?q=$site;
tput smso;
 tput blink;
tput setaf 1;
tput bold;
echo $'\nPress any key to continue';
tput sgr0;
read key;
clear
./EternalView.sh;
 elif [[ opt -eq '10' ]]; # HTTP HEADER
 then tput setaf 10;
echo -en "Enter the website address (without http://): ";
read site;
curl -I $h$site;
tput smso;
 tput blink;
tput setaf 1;
tput bold;
echo "Press any key to continue";
tput sgr0;
read key;
clear
./EternalView.sh;
 elif [[ opt -eq '11' ]]; # TRACEROUTE
 then tput setaf 9;
echo -en "Enter the website or IP address: ";
read site;
traceroute $site;
tput smso;
tput blink;
tput setaf 1;
tput bold;
echo "Press any key to continue";
tput sgr0;
read key;
clear
./EternalView.sh;
 elif [[ opt -eq '12' ]]; #AUTOPWN
 then tput setaf 12;
 echo "Make sure that Autopwn is in the same folder";
 chmod +x Autopwn.sh;
./Autopwn.sh;
clear
./EternalView.sh;
 elif [[ opt -eq '13' ]]; #RELOAD
 then clear
./EternalView.sh;
 elif [[ opt -eq '14' ]]; #EXIT
 then clear;
 exit;
else
	tput smso;
	tput blink;
	tput setaf 1;
	tput bold;
	echo "Please choose a valid option! Press Enter to continue";
	tput sgr0;
	read key;
	clear
	./EternalView.sh;
 fi;
