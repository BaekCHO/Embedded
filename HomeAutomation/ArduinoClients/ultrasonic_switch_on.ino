#include <Servo.h>
#include "Ultrasonic.h"

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

Ultrasonic us(7);
// The output port of ultra sonic is 7

int pos = 0;    // variable to store the servo position

int led = 13;
int value;
int i;
int threshold = 1600;
int sensorvalue[20] = {0};
int sum = 0;
int avg;
int degree = 5;
boolean toward = true;
long rangeInCentimeters;

void setup() {    
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  pinMode(2, INPUT);
  myservo.attach(6);  // attaches the servo on pin 9 to the servo object
  myservo.write(90);
}
 
void loop() {
  
//  long rangeInCentimeters;
  rangeInCentimeters = us.MeasureInCentimeters();
  
  /*
  if(rangeInCentimeters < 100){
    digitalWrite(13, LOW);
    Serial.print(rangeInCentimeters);
    Serial.print("\n");
  }
  */
  
  for(i = 0; i < 20; i++){
    sensorvalue[i] = analogRead(A0);
  }
  
  for(i = 0; i < 20; i++){
    sum += sensorvalue[i];
  }
  
  avg = sum / 20;
  
  if(avg > threshold && rangeInCentimeters > 100){
    digitalWrite(13, HIGH);
    Serial.print(avg);
    Serial.print("\n");
  } else if(avg > threshold && rangeInCentimeters < 100){
    digitalWrite(13, LOW);
  }
  
  /*
  if(rangeInCentimeters > 10){
    digitalWrite(13, HIGH); //Turn ON Led
    Serial.print(avg);
    Serial.print("\n");

    if(toward == true){ // turn on the switch
      degree = 180;
      myservo.write(degree);
      delay(1000);
      myservo.write(90);
      toward = false;
    } else if(toward == false){ // turn off the switch
      degree = 5;
      myservo.write(degree);
      delay(1000);
      myservo.write(90);
      toward = true;
    }
  }
  */
}
