## ___  __             __       ___       ___  ___                
##|__  /  \ |    |    /  \ |  |  |  |__| |__  |__  |  | |     /\  
##|    \__/ |___ |___ \__/ |/\|  |  |  | |___ |___ \__/ |___ /~~\ 
##                                                                
##
## Programmed By: Reecepbcups - August 25th 2018
##
## This program is used to gather Minecraft server EULA block bypasses.
## This is usually done by using a ddns.net domain to relink the main domain to the server IP. (Main IP -> New.ddns.net -> Server IP Address)
## This programs aims to stop this with a more automated way of banning these bypasses and provides an easy output into a txt file.
##
## How to Run ###
##1. Run main(), which will call the grab_all_blocked_Servers(), check(), and outputToFile() functions
##2. IPs in the Bypassed_Ips.txt file need to be blocked as they are bypassing the block :)

import requests, json         # Sudo pip install request, json, pprint 
from pprint import pprint


url = 'https://use.gameapis.net/mc/extra/blockedservers/text'     # Grabs the list of blocked servers from the gameapis website
r = requests.get(url)                                             # saves the page conects (HASH+IP) to the variable "r"


def outputToFile():                 # Function to output the servers to a file
      import urllib2, html2text     # imports 2 modeules used for HTML work
      
      page = urllib2.urlopen(url)                           # opens the url and saves it to "page" variable used only in this function
      html_content = page.read()                            # saves the page to "html_conent" variable
      rendered_content = html2text.html2text(html_content)  # Does some other HTml save stuff thats needed for this
      
      file = open('blockedServersList.txt', 'w')            # Created file, or opens if its already there
      file.write(rendered_content)                          # Saves all the blocked servers into a text file named "blockedServersList.txt"
      file.close()                                          # closes and saves

    
ips = [] # an empty list of IP's, will be used in the grab_all_blocked_Servers() function below

def grab_all_blocked_Servers():
      with open('blockedServersList.txt') as f:                               # opens the blockedServerListFile with all blocked Ips and hashes as the variable "f"
          blockedServers = f.readlines()                                      # reads all the data from the text file into a list, and saves to the blockedServers variable                     

      for i in range(len(blockedServers)):                                   
            try: 
                  data = blockedServers[i].split(":")[1].replace("*.", "")    # Seperates the Hash from the IP at the semicolon. Then selects index 1 (the IP address), and replaces *. to nothing if it is by itself
                  ips.append(data)                                            # add the above variable to the temperary ip's variable above this function (seen with ips[0] or any other index)        
            except: 
                  continue

            
alreadyBeenChecked = []       # save already checked ips so there are no duplicated ips in output
def check(server):            # check server function, with ability to pass the server ip through !!(run check('ServerIPAddress.com') to just check 1)!!
      
      url = 'https://use.gameapis.net/mc/extra/blockedservers/check/' + server      # grabs domain, sha1, and blocked json files tracker
      r = requests.get(url)                                                         # saves this url as a temp r variable
      data = r.json()                                                                # saves the page to the data variable as a json format
 
      try: 
            for i in range(50):                                               #Loops 50 times for an index to grab from
                  f = open("Bypassed_IPs.txt", 'a')                           #opens the Bypassed IPs file to be able to append too. This means any IPs in this file before will still be there after a re-run
                  isItBlocked = data[server][i]['blocked']                    # checks server block status (returns True or False)
                  ip = data[server][i]['domain'].encode('ascii','ignore')     # grabs the domain address and changed from unicode to normal text

                  
                  if isItBlocked == False:                                    # Makes sure the server is not blocked yet
                        if "*.ddns.net" not in ip and "*.dynu.net" not in ip: # checks if the ip is not blocked, and it is not just *.ddns.net, or *.dynu.net.
                              if "*." != ip and "" != ip:                     # checks to make sure its not just a "*." or just a blank line
                                    if ip.endswith("-") != True:              # makes sure it ends with a .domain, and not just a - as some longer domains mess up
                                          if ip not in alreadyBeenChecked:
                                                print(ip)                           # prints IP to the python console
                                                f.write(ip + "\n")                  # writes this IP into the text file
                                                alreadyBeenChecked.append(ip)       # adds to the lready checked list
                        
      except IndexError:      # if the index is out of range (ex. only 3 json contains and its on loop 4)
            f.close()         # saves the file with the additions of that server



def main():                         # the main function, for a new rerun
      print("Making/ReWriting blocked domains to file...")
      outputToFile()                # outputs banned servers into a text file
      print("loading in all blocked domains...")
      grab_all_blocked_Servers()    # opens the BlockedServer IP list from the text file, and adds to the ips list
      
      print("\nServer Bypasses IP's:")
      for i in range(len(ips)):                             # runs a loop based on the number of ips in the blocked list
            Server_To_Check = ips[i].replace("\n", "")      # replaces all the new line characters to nothing for every IP
            check(Server_To_Check)                          # checks the ip in that index, and goes to check() function

