
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
    os.system('xdg-open https://chat.whatsapp.com/E9G45DzibkCJe42rCnaiKi/');time.sleep(5)
    from Xplus import Xplus
    Xplus()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
