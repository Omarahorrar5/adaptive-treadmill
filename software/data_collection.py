# Python code to read serial data from Arduino and plot the raw PPG signal

import serial
import numpy as np
import matplotlib.pyplot as plt
import time

# Open serial connection
arduino_data = serial.Serial('COM7', 9600)

collection_duration = 10  # seconds
data = []
timestamps = []

start_time = time.time()

while time.time() - start_time < collection_duration:
    try:
        raw_value = arduino_data.readline().decode('utf-8').strip()
        value = float(raw_value)
        elapsed_time = time.time() - start_time

        data.append(value)
        timestamps.append(elapsed_time)

    except ValueError:
        continue

arduino_data.close()

# Plotting
plt.plot(timestamps, data)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Raw PPG Signal')
plt.grid(True)
plt.show()
