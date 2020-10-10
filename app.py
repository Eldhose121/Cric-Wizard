from pyautogui import locateOnScreen
from time import sleep
from winsound import Beep
from boltiot import Bolt
import bdetails
import json



bolt_inst = Bolt(bdetails.API_KEY, bdetails.DEVICE_ID)



def alert_user():
 bolt_inst.digitalWrite('0', 'HIGH')
 sleep(0.25)
 bolt_inst.digitalWrite('0', 'LOW')



def main():
 print("Hello!, pls minimize this screen and open the live score in 5 seconds...")
 online = False
 resp = bolt_inst.isOnline()
 msg = json.loads(resp)
 if(msg['value']=='online'):
     online = True
 sleep(5)
 while True:
  try:
   wloc = locateOnScreen('images/wicket.png')
   sloc = locateOnScreen('images/six.png')
   if wloc or sloc:
    if online:
     alert_user()
    else:
     print("Device offline or invalid device credentials!")
    sleep(60)
   sleep(5)
  except Exception as e:
   print(e)
   sleep(5)



if __name__ == '__main__':
 main()
