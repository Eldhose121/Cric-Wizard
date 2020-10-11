# Cric-Wizard

### By Team Zeta_Codinators

  Cric-Wizard identifies important events in a cricket match for example when a six has been scored or if a wicket has been lost and alerts the user regarding the same. It is particularly useful if the user is concentrating on studies or some other work and would like to be notified of only the most important events without getting distracted from his/her work. It also helps avoid the need for mobile phones for the purpose which are quite distractive in nature. 

<br />

  Cric-Wizard makes use of a Bolt WiFi Module and an Arduino for the purpose. Being IoT-based, it can be effortlessly setup anywhere the user wishes to. A python program is used which uses some facile image recognition techniques to identify whether an event has occured and rings a buzzer on the Bolt module. It then communicates via UART with the Arduino which display whichever event has occured through the LCD screen. Hence the user is notified about the event.
  

## Cric-Wizard Setup

### Hardware setup

- The list of required hardware components are given in [components](Hardware-Components.csv).
- Connnect the components according to the circuit shown below at a convenient location and connect to power.

 <br />
 
![circuit](Circuit-Diagram.jpg?raw=true)

<br/>

### Install dependencies

```
$ pip install pyautogui
$ pip install boltiot
```

### Clone the repo

```
$ git clone https://github.com/alanphil2k01/Cric-Wizard
$ cd Cric-Wizard
```

### Run Cric-Wizard

- Upload the code given in the Arduino directory onto your Arduino board.
- Keep the live scoreboard open in a chrome tab.
- Run the program.

```
$ python app.py
```

Now you can focus on your work and Cric-Wizard shall automatically notify you if any important events have occured.
<br/>
Enjoy the Cric-Wizard experience!
