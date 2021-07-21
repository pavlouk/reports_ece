#include <Servo.h>

Servo myServo;
Servo myServo2;
int value;
int angle;

void servoWrite( int angle, int servo) {
  
  int  transistorPin;

  if (servo == 1) {
    transistorPin = 10;
  } else {
    transistorPin = 11;
  }

  if (angle >180) {

    double t = (139/90.0) * (angle/2.0);
    
    digitalWrite(transistorPin,HIGH);
    
    if (servo == 1) {
      myServo.write(180);
    } else {
      myServo2.write(180);
    }
    
    delay(t);
    digitalWrite(transistorPin,LOW);
    delay(30);
    digitalWrite(transistorPin,HIGH);
    
    if (servo == 1) {
      myServo.write(180);
    } else {
      myServo2.write(180);
    }
    
    delay(t);
    digitalWrite(transistorPin,LOW);
  
  } else {

    double t = (142/90.0) * angle;
    
    digitalWrite(transistorPin,HIGH);
    
    if (servo == 1) {
      myServo.write(180);
    } else {
      myServo2.write(180);
    }
    
    delay(t);
    digitalWrite(transistorPin,LOW);
  }

  delay(500);
}


void setup() {
  Serial.begin(9600);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  myServo.attach(9);
  myServo2.attach(12);
  
  servoWrite(60,1);
  //servoWrite(90,2);
  delay(500);
}

void loop() {
  //servoWrite(90,1);
  //servoWrite(90,2);
  delay(100);
}