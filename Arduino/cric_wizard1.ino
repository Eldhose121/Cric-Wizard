#include <LiquidCrystal.h>

LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

void cricket(int stat){
    if(stat==0){
      	lcd.clear();
        lcd.print("no new event");
        delay(5000);
    }
    if(stat==1){
		lcd.clear();
        lcd.print("SIX!!");
        delay(5000);
    }
    if(stat==2){
        lcd.clear();
        lcd.print("OUT!!");
        delay(5000);
    }
}


void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);

}

void loop() {
  if(Serial.available()){
    int stat = Serial.read()-'0';
    if(stat>=0 && stat<=2){
        cricket(stat);
    }
    else{
        Serial.println("Invalid Status.");
    }
  }
}