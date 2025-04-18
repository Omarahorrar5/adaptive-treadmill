int vitessePin = 5;  // PWM pin connected to motor driver
int dir1 = 4;        // Direction control pin 1
int dir2 = 3;        // Direction control pin 2
int vitesse = 0;     // Motor speed (0-255)

void setup() {
  pinMode(vitessePin, OUTPUT);
  pinMode(dir1, OUTPUT);
  pinMode(dir2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    vitesse = Serial.parseInt();

    if (vitesse != 0) {
      // Set motor direction
      digitalWrite(dir1, LOW);
      digitalWrite(dir2, HIGH);

      // Apply PWM signal to control motor speed
      analogWrite(vitessePin, vitesse);
    }
  }
}
