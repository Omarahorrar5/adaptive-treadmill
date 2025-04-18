# Python function to perform FFT (Fast Fourier Transform) to get the frequency spectrum of a filtered PPG signal

import numpy as np
import matplotlib.pyplot as plt

def FFT(signal, Te):
    frequencies = np.fft.rfftfreq(len(signal), Te)
    spectrum = np.abs(np.fft.rfft(signal))
    return frequencies, spectrum