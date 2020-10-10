from time import sleep
from winsound import Beep
from pyautogui import screenshot
import pytesseract
from boltiot import Bolt
import bdetails


bolt_inst = Bolt(bdetails.API_KEY, bdetails.DEVICE_ID)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user1\AppData\Local\Tesseract-OCR\tesseract.exe'



def alert_user():
    Beep(500, 5000)



def main():
    print("Please minimize this screen and open the live score page in 5 seconds....")
    sleep(5)
    data = {}
    data["w1"]=0
    data["w2"]=0
    w1=0
    w2=0
    while True:
        im = screenshot('images/img.png', region=(438,169,945,333))
        text = pytesseract.image_to_string(im)
        c=0
        lc=0
        for l in text:
            if l=='/':
                if lc:
                    w2=int(text[c+1])
                else:
                    w1=int(text[c+1])
            ++c
        if w1!=data["w1"] or w2!=data["w2"]:
            data["w1"]=w1
            data["w2"]=w2
            alert_user()
            print(w1,w2)
        else:
            print("No")
        sleep(10)

if __name__ == '__main__':
    main()
