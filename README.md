A python 2.7 program to check for servers bypassing the Mojang domain ban

#Follow The EULA#
                                                                

Programmed By: Reecepbcups - August 25th 2018


 This program is used to gather Minecraft server EULA block bypasses.
 This is usually done by using a ddns.net domain to relink the main domain to the server IP. (Main IP -> New.ddns.net -> Server IP Address)
 This programs aims to stop this with a more automated way of banning these bypasses and provides an easy output into a txt file.

# How to Run ###
1. Run main(), which will call the outputToFile(), ab_all_blocked_Servers(), and check() functions
2. IPs in the Bypassed_Ips.txt file need to be blocked as they are bypassing using the DNS work around :)

#What You Need installed#
You Will need to have: 
  Python 2.x.x
  request, json, pprint modules (Sudo pip install request, json, pprint)
