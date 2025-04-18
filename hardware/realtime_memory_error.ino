// Arduino Nano - Real-Time FFT (Causes memory issues)

#include <FFT.h>

const int analogPin = A0;
const int sampleSize = 128;  // Large buffer size for FFT

float signal[sampleSize];
float spectrum[sampleSize / 2];

unsigned long lastSampleTime = 0;
unsigned long sampleInterval = 1000 / 100;  // 100 Hz sampling rate

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Sample signal
  for (int i = 0; i < sampleSize; i++) {
    unsigned long currentTime = millis();
    while (millis() - currentTime < sampleInterval);  // wait for next sample
    signal[i] = analogRead(analogPin);
  }

  // Apply FFT (this is where memory usage spikes)
  FFT(signal, sampleSize, spectrum);  // Placeholder function

  // Find peak frequency
  float maxVal = 0;
  int maxIndex = 0;
  for (int i = 0; i < sampleSize / 2; i++) {
    if (spectrum[i] > maxVal) {
      maxVal = spectrum[i];
      maxIndex = i;
    }
  }

  // Estimate heart rate
  float freqResolution = 100.0 / sampleSize;  // fs / N
  float dominantFreq = maxIndex * freqResolution;
  float heartRate = dominantFreq * 60;

  // Output
  Serial.print("Heart Rate: ");
  Serial.print(heartRate);
  Serial.println(" BPM");
}
