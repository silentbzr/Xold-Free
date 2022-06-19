
import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations Your Device Support This Tool\033[1;37m")
    print("\n\033[1;37m Kisi Ko Bhee Apny Name Ki OLD I'ds - Public Cloning - Number Cloning Command Bnwani Ho to Admin sy WhatsApp py Rabta Karein Thanku Janiezz :)") 

    print("\n\n\x1b[1;91m System Loading Please Wait...")
    os.system('xdg-open https://www.facebook.com/hellin.786/');time.sleep(10)
    from Xplus import Main
    Main()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
