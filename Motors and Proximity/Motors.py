#include <Servo.h> //include ur servo library here

Servo myservo;

int servoPin = 9;


void sertup() {
  myServo.attach(servoPin);
}


Voide loop() {
  //move servo to 0 degrees
  myServo.write(0);
  delay(1000); //wait one sec then start

  //move servo to 90 degrees
  myServo.write(90);
  delay(1000);

  //move servo to 90 degrees
  myServo.write(180);
  delay(1000);

}

# motion sensor

//define our signal pin
const int sensorPin = 7;

void setup(){
  //starting the serial 
  Serial.begin(9600);
  //setting our sensor pin as input
  pinMode(sensorPin, INPUT);
}

void loop() {
  //read the sensor value 
  int sensorValue = digitalRead(sensorPin);

  //checking if motion is present/detected
  if (sensorValue == HIGH) {
    while (digitalRead(sensorPin) == HIGH) {
      Serial.print("Motion is detected yayy");
      delay(500); //adjust the delay message frequency
    }
  } else {
    Serial.println("no motion boohoo."); // Corrected the print function
    delay(500);
  }
}
