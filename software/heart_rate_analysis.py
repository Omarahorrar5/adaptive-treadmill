# Python code to collect PPG data over an extended period for heart rate analysis

import serial
import numpy as np
import time
from scipy import signal
import matplotlib.pyplot as plt

# Bandpass filter parameters
low_cutoff = 0.83   # Hz (≈ 50 BPM)
high_cutoff = 3.33  # Hz (≈ 200 BPM)
fs = 100            # Sampling frequency
Te = 1 / fs         # Sampling period

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = signal.butter(order, [lowcut, highcut], btype='band', fs=fs)
    return signal.lfilter(b, a, data)

# Serial setup
arduino = serial.Serial('COM7', 9600)

duration = 60  # one minute
data = []
timestamps = []
start_time = time.time()

while time.time() - start_time < duration:
    try:
        value = float(arduino.readline().decode('utf-8').strip())
        current_time = time.time() - start_time
        data.append(value)
        timestamps.append(current_time)
    except ValueError:
        continue

arduino.close()

# Centering the signal (remove DC offset)
mean_value = np.mean(data)
centered_data = [x - mean_value for x in data]

# Apply bandpass filter
filtered_data = bandpass_filter(centered_data, low_cutoff, high_cutoff, fs)

# FFT
def FFT(signal, Te):
    freqs = np.fft.rfftfreq(len(signal), Te)
    spectrum = np.abs(np.fft.rfft(signal))
    return freqs, spectrum

frequencies, spectrum = FFT(filtered_data, Te)
fundamental_freq = frequencies[np.argmax(spectrum)]
heart_rate = fundamental_freq * 60

plt.plot(timestamps, filtered_data)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Filtered PPG Signal Over Time")
plt.grid(True)
plt.show()

print(f"Estimated Heart Rate: {heart_rate:.2f} BPM")
