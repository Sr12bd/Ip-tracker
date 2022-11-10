import requests
import pyfiglet
import time
import colorama
from colorama import*
banner = pyfiglet.figlet_format("Ip tracker")
print(Fore.BLUE+banner)
time.sleep(0.5)
print(Fore.BLUE+"reading ip addreses........")
time.sleep(0.5)
cont=input(Fore.BLUE+"press Enter to continue:")
print("\n")
responce = requests.post("http://ip-api.com/batch" , json=[

  {"query": "208.80.152.201"},
  {"query": "167.71.3.52"},
  {"query": "206.189.198.234"},
  {"query": "157.230.75.212"}
]).json()
for ip_info in responce:

    
    
    print(Fore.GREEN+"Latitude & longtitude:" ,ip_info["lat"] ,ip_info ["lon"])
    time.sleep(0.3)
    print(Fore.GREEN+"Country:" , ip_info["country"])
    time.sleep(0.3)
    print(Fore.GREEN+"City:" , ip_info["city"])
    time.sleep(0.3)
    print(Fore.GREEN+"Zip:", ip_info ["zip"])
    time.sleep(0.3)
    print(Fore.GREEN+"--------------------------------------------------")

    print("\n")




