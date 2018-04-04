# Network-Survival

**1. System Info Tool** - This tool will grab the hostname of the target machine.
  - This tool will need to use the socket module.
  - It will print the hostname to stdout in the format of: "The hostname is: NoSoupForYou"

**2. IP Mapping** - This tool will return the corresponding IP address of any domain entered.
  - This tool will make use of the socket module.
  - It will take stdin from the user and return the IP address in the format of: "The IP address of target is: 58.65.22.14"
    
**3. Port Scanner** - This tool will scan for open ports on any domain or IP and return a report when completed.
 - This tool will make use of the socket and sys modules.
 - It will be able to scan any range of ports.
 - It will generate a report in the format of: "Port 80: OPEN"
 
**4. Client Browser** - This tool will act as your client browswer to pull html from any domain.
  - This tool will make use of the urllib module.
  - It will be able to print the url, status code of request, request header info, server info, and the html.
      
**5. Mac Address Lookup** - This tool will return information on mac addressses.
  - This tool will use the urllib2, json, and codecs modules.
  - This tool will make an api call with mac address to http://macvendors.co/api
  - It will take stndin from user.
  - It will return a report in format of: "Company Name, Address".
  
