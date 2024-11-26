#include <Servo.h>

// Define pins for first ultrasonic sensor
const int trigPin1 = 9;
const int echoPin1 = 10;

// Define pins for second ultrasonic sensor
const int trigPin2 = 11;
const int echoPin2 = 12;

// Define pins for third ultrasonic sensor
const int trigPin3 = 6;
const int echoPin3 = 7;

// Create Servo objects
Servo myServo1;
Servo myServo2;
Servo myServo3;

// Variables for duration and distance
long duration1, duration2, duration3;
int distance1, distance2, distance3;

void setup() {
  // Set up the serial monitor
  Serial.begin(9600);

  // Set up the trig and echo pins for all three sensors
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);

  // Attach the servos to their respective pins
  myServo1.attach(3);
  myServo2.attach(5);
  myServo3.attach(A0);

  // Move the servos to their initial positions
  myServo1.write(0);
  myServo2.write(0);
  myServo3.write(0);
}

void loop() {
  // For first ultrasonic sensor
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);

  // Read the echoPin for first sensor and calculate the distance
  duration1 = pulseIn(echoPin1, HIGH);
  distance1 = duration1 * 0.034 / 2; // Convert to centimeters

  // For second ultrasonic sensor
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);

  // Read the echoPin for second sensor and calculate the distance
  duration2 = pulseIn(echoPin2, HIGH);
  distance2 = duration2 * 0.034 / 2; // Convert to centimeters

  // For third ultrasonic sensor
  digitalWrite(trigPin3, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);

  // Read the echoPin for third sensor and calculate the distance
  duration3 = pulseIn(echoPin3, HIGH);
  distance3 = duration3 * 0.034 / 2; // Convert to centimeters

  // Print distances to the serial monitor
  Serial.print("Distance 1: ");
  Serial.print(distance1);
  Serial.print(" cm, ");
  Serial.print("Distance 2: ");
  Serial.print(distance2);
  Serial.print(" cm, ");
  Serial.print("Distance 3: ");
  Serial.println(distance3);

  // For the first sensor: Check if distance is within range and map to servo angle
  if (distance1 > 0 && distance1 <= 10) {
    int angle1 = constrain(map(distance1, 5, 10, 90, 0), 0, 90);
    myServo1.write(angle1); // Move the first servo to the calculated angle
  } else {
    myServo1.write(0); // Move the first servo back to 0 degrees if out of range
  }

  // For the second sensor: Check if distance is within range and map to servo angle
  if (distance2 > 0 && distance2 <= 10) {
    int angle2 = constrain(map(distance2, 5, 10, 90, 0), 0, 90);
    myServo2.write(angle2); // Move the second servo to the calculated angle
  } else {
    myServo2.write(0); // Move the second servo back to 0 degrees if out of range
  }

  // For the third sensor: Check if distance is within range and map to servo angle
  if (distance3 > 0 && distance3 <= 10) {
  int angle3 = constrain(map(distance3, 5, 10, 90, 0), 0, 90);
  myServo3.write(angle3); // Move the third servo to the calculated angle
  } else {
  myServo3.write(0); // Move the third servo back to 0 degrees if out of range
  }


  // Delay for a short time
  delay(100);
}