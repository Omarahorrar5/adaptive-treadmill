# Adaptive Treadmill

The Adaptive Treadmill project is a real-time, heart-rate-driven treadmill control system that uses PPG (Photoplethysmography) signals acquired via Arduino and processed in Python. The system analyzes the user's heart rate using signal filtering and FFT, then uses a machine learning model to determine and control optimal treadmill speed based on cardiovascular response.

## 🧠 Project Overview

- **Goal**: Automatically adjust treadmill speed based on user's heart rate in real-time.
- **Components**:
  - Arduino Nano with a PPG sensor for signal acquisition (photoresistor)
  - Python for signal processing, heart rate detection, and ML-based speed control
  - DC Motor and Motor driver (simulation of the treadmill)

---

## 📁 Project Structure

```
adaptive-treadmill/
├─ .gitignore
├─ README.md
├─ LICENSE
├─ images/
│   └─ images/                      ← Real system photos and setup images
├─ hardware/
│   ├─ arduino_ppg.ino              ← Acquires PPG signal from analog sensor
│   ├─ motor_control.ino            ← Receives speed value via serial and drives motor
│   └─ realtime_memory_error.ino    ← FFT implementation on Arduino (memory overflow test)
├─ software/
│   ├─ data_collection.py           ← Collects raw PPG data over serial
│   ├─ filtering.py                 ← Applies bandpass filter to PPG signal
│   ├─ fft_analysis.py              ← Performs FFT to extract dominant frequency (heart rate)
│   ├─ motor_control_model.py       ← Trains ML model to predict speed from heart rate
│   └─ heart_rate_analysis.py       ← Signal aquisition for a long period, filtering, applying FFT, getting the BPM

---

## 🔧 Hardware Requirements

- Arduino Nano (or compatible board)
- PPG Sensor (photoresistor)
- Bluetooth module
- Motor driver (L298N or equivalent)
- DC motor
- USB cable and power supply

---

## 🖥️ Software Requirements

- Python 3.8+
- Arduino IDE
- Required Python libraries:
  ```bash
  pip install numpy matplotlib scipy scikit-learn pyserial
  ```

---

## 🚀 How It Works

1. **Signal Acquisition**  
   Arduino continuously reads analog PPG data and transmits it via serial.

2. **Signal Processing in Python**  
   - Raw data is collected for a defined duration.
   - A bandpass filter isolates the frequency band relevant to human heart rates (0.8–3.3 Hz).
   - FFT identifies the dominant frequency representing the heart rate.

3. **Heart Rate to Speed Mapping (ML Model)**  
   - Trained using sample data (`sample_data.txt`)
   - Predicts the optimal speed to minimize fatigue while keeping a steady cardio effort

4. **Motor Control**  
   - The predicted optimal speed is sent to the Arduino.
   - Arduino sets motor direction and PWM speed via motor driver.

---

## 🧪 Example Execution

Run the following Python scripts in order:

```bash
python data_collection.py
python filtering.py
python fft_analysis.py
python motor_control_model.py
python optimal_speed_sender.py
```

---

## 📊 Sample Output

- **Estimated Heart Rate**: 78.5 BPM
- **Predicted Optimal Speed**: 4.2 km/h
- **PWM Sent to Motor**: 145

---

## ⚠️ Known Issues

- Performing FFT directly on Arduino may exceed memory limits.
- Serial port must be correctly configured (`COMx`) based on your system.

---

## 🙌 Acknowledgments

- OpenCV and PySerial communities
- scikit-learn contributors
- Arduino documentation and forums

---