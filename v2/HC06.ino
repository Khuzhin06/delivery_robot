#include <SoftwareSerial.h>
SoftwareSerial HC06(10, 11); //HC06-TX Pin 10, HC06-RX to Arduino Pin 11

int LED = 12; //Use whatever pins you want 
int LDR = A0; //Sensor Pin to Analog A0

void setup() {
  HC06.begin(9600); //Baudrate 9600 , Choose your own baudrate 
  pinMode(LED, OUTPUT);
  pinMode(LDR, INPUT);
}

void loop() {

  if(HC06.available() > 0) //When HC06 receive something
  {
    char receive = HC06.read(); //Read from Serial Communication
    if(receive == '1')
    {
      digitalWrite(12, HIGH); 
      int data = analogRead(LDR);
      HC06.println('front');
    }
    elif(receive == '2')
    {
      digitalWrite(12, HIGH);
      int data = analogRead(LDR);
      HC06.println('back');
    }
    elif(receive == '3')
    {
      digitalWrite(12, HIGH);
      int data = analogRead(LDR);
      HC06.println('left');
    }
    elif(receive == '4')
    {
      digitalWrite(12, HIGH);
      int data = analogRead(LDR);
      HC06.println('right');
    }
    else digitalWrite(12, LOW);//If received other data, turn off LED
  }

}
