# Python function to apply band-pass filter to a PPG signal

from scipy import signal

# Band-pass filter parameters (in Hz)
low_cutoff = 0.83     # ≈ 50 BPM (min)
high_cutoff = 3.33    # ≈ 200 BPM (max)
sampling_rate = 100

def bandpass_filter(data, low_cutoff, high_cutoff, sampling_rate, order=5):
    b, a = signal.butter(order, [low_cutoff, high_cutoff], btype='band', fs=sampling_rate)
    y = signal.lfilter(b, a, data)
    return y