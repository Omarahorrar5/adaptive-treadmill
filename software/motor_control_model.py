import numpy as np
from sklearn.linear_model import LinearRegression
import serial

def load_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    heart_rate_data = []
    speed_data = []
    fatigue = []

    for i in range(0, len(lines), 3):
        heart_rates = eval(lines[i].strip())
        speeds = eval(lines[i+1].strip())
        fatigue_level = int(lines[i+2].strip())

        heart_rate_data.append(heart_rates)
        speed_data.append(speeds)
        fatigue.append(fatigue_level)

    return heart_rate_data, speed_data, fatigue

# Load data (heart rate, speed, and fatigue levels)
file_path = "C:\\Users\\User\\Desktop\\data.txt"
heart_rate_data, speed_data, fatigue = load_data(file_path)

# Prepare features (X) and targets (y)
X = np.array([np.mean(speeds) for speeds in speed_data]).reshape(-1, 1)
y = np.array([max(hr) for hr in heart_rate_data])

# Train model
model = LinearRegression()
model.fit(X, y)

# Model parameters
slope = model.coef_[0]
intercept = model.intercept_

# Predict optimal heart rate from non-fatigued sessions
valid_indices = [i for i, f in enumerate(fatigue) if f == 0]
X_valid = np.array([np.mean(speed_data[i]) for i in valid_indices]).reshape(-1, 1)
predicted_hrs = model.predict(X_valid)

optimal_hr = np.mean(predicted_hrs)
optimal_speed = (optimal_hr - intercept) / slope

# Convert optimal speed to control signal (0–255)
speed_min = min(min(x) for x in speed_data)
speed_max = max(max(x) for x in speed_data)
tension_min = 0
tension_max = 255

motor_signal = np.interp(optimal_speed, [speed_min, speed_max], [tension_min, tension_max])

# Send control signal to Arduino
ser = serial.Serial("COM7", 9600)
ser.write(str(round(motor_signal)).encode())
ser.close()
