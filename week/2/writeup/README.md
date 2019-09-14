# Writeup 2 - OSINT

Name: Cooper Willetts
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Cooper Willetts

## Assignment Writeup

### Part 1 (45 pts)

Ejnorman84
1. Real Name: Eric Norman 
    -Was able to Obtain his real name by going to UMD Cyber Security Club twitter, looking at who followed, then searching for ejnorman which brought me to his personal page.

2. Work: Wattsamp Energy http://wattsamp.net/views/about.html 
    -Able to pull this information in his twitter bio from above. 
    -Also found his instagram that links to this page and company

3. Personal Information (Socials, contacts) :
    Twitter: https://twitter.com/EricNorman84
        Was able to Obtain his real name by going to UMD Cyber Security Club twitter, looking at who followed, then searching for ejnorman which brought me to his personal page.
    Emails: ejnorman84@gmail.com, ejnorman@protonmail.com 
        Found Emails in a tweet from Twitter
    Instagram - @ejnorman84	
        Used instagram search to look for @ejnorman84
    Address - 1300 Adabel Dr, El Paso, TX 79835
        whois wattsamp.net
    Phone Number - 2026562837
        Whois wattsamp.net 

4. IP: 157.230.179.99
    Location: North Bergen, New Jersey, United States (US) 
    Provider: Digital Ocean 
        Discovered both by using Censys - https://censys.io/ipv4/157.230.179.99 
    Dns History 
        Not alot of DNS history, created 4 days ago 
        Found using Dns trails
        https://securitytrails.com/domain/wattsamp.net/history/a

5. HIdden files and Directories on website: 


6. pen Ports :
    22 - ssh 
        Found by using nmap -v -A wattsamp.net
    80 - http 
        Found by usng nmap -v -A wattsamp.net
    1337 
        Found using nmap -v -9 1000-1500 

7. Server:
    Linux,  Ubuntu 
        Found by using Nmap -v -A wattsamp.net
        Verified by https://censys.io/ipv4/157.230.179.99  


Bonus Flags
*CMSC389R-{html_h@x0r_lulz}
    view-source:http://wattsamp.net/ 
*CMSC389R-{n0_indexing_pls}
    http://wattsamp.net/robots.txt
*CMSC389R-{Do_you-N0T_See_this} 
    https://securitytrails.com/domain/wattsamp.net/dns 


### Part 2 (75 pts)

Part 2 - 
I was not able to gain proper login credentials to the server nor find the final flag, but I will still document my progress how I approached the problem.

My Progress: 
	I was able to develop a script that automatically tests passwords within the text file. If you run this, you will see that it works properly and begins testing each password with the username given. I am unaware if I am using the wrong username or doing something incorrectly to detect if a combination yields a proper success. 

