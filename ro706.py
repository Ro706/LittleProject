import datetime
import time
from termcolor import colored
import wikipedia
import webbrowser
import os
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
def phone():
    os.system('figlet phone number')
    print(colored('================================','cyan'))
    # Parsing String to Phone number
    a=str(input(colored('enter number: ','green')))
    print(colored('''=======================
[      TIME ZONE      ]
======================= ''','green'))
    phoneNumber = phonenumbers.parse(a)
    # Pass the parsed phone number in below function
    timeZone = timezone.time_zones_for_number(phoneNumber)
    time.sleep(1)

    # It print the timezone of a phonenumber
    print(colored(timeZone,'yellow'))
    print(colored('''=======================
[      NETWORK        ]
======================= ''','green'))
    ro_number = phonenumbers.parse(a, "RO")
    time.sleep(1)

    print(colored(carrier.name_for_number(ro_number, "en"),'yellow'))
    print(colored('''=======================
[      GEOLOCATION    ]
======================= ''','green'))
    ch_number = phonenumbers.parse(a, "CH")
    time.sleep(1)
    print(colored(geocoder.description_for_number(ch_number, "en"),'yellow'))
def AboutMe():
    print (colored('https://github.com/Ro706','yellow'))
    print (colored('Name: Ro706','yellow'))
    print (colored('version 1.Ro706','blue'))
def webbrowser():
    os.system('lynx https://www.google.com')
def wiki():
    return wikipedia.summary(input('#wiki >> '))
def options():
    print (colored('1) Google ','blue'))
    print (colored('2) Wikipedia','blue'))
    print (colored('3) About Me','blue'))
    print (colored('4) phone_info ','blue'))
    print (colored('5) Exit','blue'))
def wishme():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        print (colored('Good morning','yellow'))
    elif time >= 12 and time < 16:
        print (colored('Good afternoon','yellow'))
    else:
        print (colored('Good evening','yellow'))
os.system('clear')
wishme()
options()
loop = 1
choice = 0
while loop==1:
  choice = str(input('#Ro706>> '))
  if choice == '1':
      webbrowser()
  elif choice == '2':
      wiki()
  elif choice == '3':
      AboutMe()
  elif choice == '4':
      phone()
  elif choice == 'ls':
      options()
  elif choice == '5':
      break
  else:
      print (colored('Error','red'))
 
