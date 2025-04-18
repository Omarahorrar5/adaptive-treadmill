// Arduino code to read analog PPG signal and send via Serial

const int analogPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(analogPin);  // Read analog value from sensor (Photoresistor)
  Serial.println(value);              // Send value to serial port
  delay(10);                          // Small delay for smoother reading
}
