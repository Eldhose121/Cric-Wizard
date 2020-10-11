from pyautogui import locateOnScreen, scroll
from time import sleep
from winsound import Beep
from boltiot import Bolt
import bdetails
import json



bolt_inst = Bolt(bdetails.API_KEY, bdetails.DEVICE_ID)



def alert_user(code):
 bolt_inst.digitalWrite('0', 'HIGH')
 bolt_inst.serialWrite(code)
 sleep(0.5)
 bolt_inst.digitalWrite('0', 'LOW')



def main():
 print("Hello!, pls minimize this screen and open the live score in 5 seconds...")
 online = False
 resp = bolt_inst.isOnline()
 msg = json.loads(resp)
 if(msg['value']=='online'):
     online = True
     bolt_inst.serialBegin('9600')
 sleep(5)
 scroll(-200)
 while True:
  try:
   wloc = locateOnScreen('images/wicket.png')
   sloc = locateOnScreen('images/six.png')
   if wloc or sloc:
    if wloc and online:
     alert_user('2')
    if sloc and online:
     alert_user('1')
    sleep(60)
    bolt_inst.serialWrite('0')
    if not online:
     print("Device offline or invalid device credentials!")
   sleep(5)
  except Exception as e:
   print(e)
   sleep(5)



if __name__ == '__main__':
 main()
