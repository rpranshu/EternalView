#!/bin/bash
resize -s 27 88
clear
tput setaf 214;
echo '                      -= Built with <3 by PRANSHU RANAKOTI  ©2018 =-';tput setaf 48;
echo '
███████╗████████╗███████╗██████╗ ███╗   ██╗ █████╗ ██╗    ██╗   ██╗██╗███████╗██╗    ██╗
██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔══██╗██║    ██║   ██║██║██╔════╝██║    ██║
█████╗     ██║   █████╗  ██████╔╝██╔██╗ ██║███████║██║    ██║   ██║██║█████╗  ██║ █╗ ██║
██╔══╝     ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║    ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║
███████╗   ██║   ███████╗██║  ██║██║ ╚████║██║  ██║███████╗╚████╔╝ ██║███████╗╚███╔███╔╝
╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝
';tput sgr0;tput setaf 50;
echo '          Welcome to EternalView™, the all-seeing ᒡ◯ᵔ◯ᒢ information gathering tool!
';tput sgr0;tput setaf 50;
echo -en '**************';tput sgr0;tput setaf 214;tput bold;echo -en 'M';tput sgr0;tput setaf 215;tput bold;echo -en 'E';tput sgr0; tput setaf 216;tput bold;echo -en 'N';tput sgr0; tput setaf 217;tput bold;echo -en 'U';tput sgr0;tput setaf 50;echo -en '**************
*';tput sgr0;tput setaf 2;
echo -en ' 1. Whois information         ';tput sgr0;tput setaf 50;echo '*';tput sgr0;
tput setaf 50;echo -en '*';tput setaf 197;
echo -en ' 2. DNS Lookup';tput sgr0;tput setaf 50;echo '                *'
tput setaf 50;echo -en '*';tput setaf 3;
echo -en ' 3. Web Technology Detection';tput sgr0;tput setaf 50;echo '  *';
tput setaf 50;echo -en '*';tput setaf 6;
echo -en ' 4. IP Locator              ';tput sgr0;tput setaf 50;echo '  *';
tput setaf 50;echo -en '*';tput setaf 5;
echo -en ' 5. NMAP                    ';tput sgr0;tput setaf 50;echo '  *';
tput setaf 50;echo -en '*';tput setaf 202;
echo -en ' 6. Robots.txt enumeration  ';tput sgr0;tput setaf 50;echo '  *';
tput setaf 50;echo -en '*';tput setaf 7;
echo -en ' 7. Pages                   ';tput sgr0;tput setaf 50;echo '  *';
tput setaf 50;echo -en '*';tput setaf 10;
echo -en ' 8. HTTP Header             ';tput sgr0;tput setaf 50;echo '  *';
tput setaf 50;echo -en '*';tput setaf 9;
echo -en ' 9. Traceroute              ';tput sgr0;tput setaf 50;echo '  *';
tput setaf 50;echo -en '*';tput setaf 11;
echo -en ' 10. AutoPwn™               ';tput sgr0;tput setaf 50;echo '  *';
tput setaf 50;echo -en '*';tput setaf 12;
echo -en ' 11. Reload                 ';tput sgr0;tput setaf 50;echo '  *';
tput setaf 50;echo -en '*';tput setaf 1;
echo -en ' 12. exit                   ';tput sgr0;tput setaf 50;echo -en '  *';
tput setaf 50;echo '
********************************';tput sgr0;
tput setaf 50;
echo -en "What would you like to do? ";tput sgr0;tput setaf 50;
read opt
 if [[ opt -eq  '1' ]]; then
    tput setaf 2;
    echo -en "Enter the website or IP address: "
    read site
    whois $site
    tput smso; tput blink;tput setaf 1;tput bold;echo "Press any key to continue";tput sgr0;
    read key
    ./EternalView
 elif [[ opt -eq '2' ]]; then
    tput setaf 197;
    echo -en "Enter the website or IP address: "
    tput setaf 50;read site;tput sgr0;
    host -a $site
    tput smso; tput blink;tput setaf 1;tput bold;echo "Press any key to continue";tput sgr0;
    read key
    ./EternalView
 elif [[ opt -eq '3' ]]; then
    tput setaf 3;
    echo -en "Enter the website or IP address: "
    read site
    wget -q https://builtwith.com/$site -O log.html
    echo "    The output has been saved as 'log.html' at"; pwd
    echo "    Please open the file log.html in your web browser to view the results!"
    tput smso; tput blink;tput setaf 1;tput bold;echo "    Press any key to continue";tput sgr0;
    read key
    ./EternalView
elif [[ opt -eq '4' ]]; then
    tput setaf 6;
    echo -en "Enter the IP address of the website: "
    read ip
    curl ipinfo.io/$ip
    tput smso; tput blink;tput setaf 1;tput bold;echo "Press any key to continue";tput sgr0;
    read key
    ./EternalView
elif [[ opt -eq '5' ]]; then
    tput setaf 5;
    echo -en "Press 1 for basic scan and 2 for extensive scan: "
    read scan
    if [[ scan -eq "1" ]]; then
        echo -en "Enter the IP address or the website address: "
        read site
        nmap $site
        tput smso; tput blink;tput setaf 1;tput bold;echo "If the Host is down or blocking the ping probes, try the extensive scan(option 2). Press any key to continue";tput sgr0;
        read key
        ./EternalView
    elif [[ scan -eq "2" ]]; then
        echo -en "Enter the IP address or the website address: "
        read site
        echo "THIS SCAN WILL TAKE SOME TIME, SIT BACK AND RELAX!"
        sudo nmap -sS -sV -v -p 1-65535 -T4 -O $site
        tput smso; tput blink;tput setaf 1;tput bold;echo "Press any key to continue";tput sgr0;
        read key
        ./EternalView
    fi
    clear
elif [[ opt -eq '6' ]]; then
    tput setaf 202;
    echo -en "Enter the website address (DNS only): "
    read site
    robo="/robots.txt"
    curl $site$robo
    tput smso; tput blink;tput setaf 1;tput bold;echo "Press any key to continue";tput sgr0;
    read key
    ./EternalView
elif [[ opt -eq '7' ]]; then
    tput setaf 7;
    echo -en "Enter the website or IP address: "
    read site
    curl https://api.hackertarget.com/pagelinks/?q=$site
    tput smso; tput blink;tput setaf 1;tput bold;echo "Press any key to continue";tput sgr0;
    read key
    ./EternalView
elif [[ opt -eq '8' ]]; then
    tput setaf 10;
    echo -en "Enter the website address (without http://): "
    read site
    curl -I $h$site
    tput smso; tput blink;tput setaf 1;tput bold;echo "Press any key to continue";tput sgr0;
    read key
    ./EternalView
elif [[ opt -eq '9' ]]; then
    tput setaf 9;
    echo -en "Enter the website or IP address: "
    read site
    traceroute $site
    tput smso; tput blink;tput setaf 1;tput bold;echo "Press any key to continue";tput sgr0;
    read key
    ./EternalView
elif [[ opt -eq '10' ]]; then
    tput setaf 12;
    {
        ./Autopwn
        ./EternalView

    } || {
        echo "Make sure that Autopwn is in the same folder"; tput sgr0;
        ./EternalView
    }
elif [[ opt -eq '11' ]]; then
    ./EternalView
elif [[ opt -eq '121' ]]; then
    clear
    exit
fi