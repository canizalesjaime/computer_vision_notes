import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Create the signal
# -----------------------------
fs = 100  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)

# Signal: 2 Hz + 5 Hz
x = np.sin(2*np.pi*2*t) + np.sin(2*np.pi*5*t)

# -----------------------------
# Step 2: Plot time domain
# -----------------------------
plt.figure()
plt.plot(t, x)
plt.title("Time Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# -----------------------------
# Step 3: Apply FFT
# -----------------------------
X = np.fft.fft(x)

# -----------------------------
# Step 4: Get frequencies
# -----------------------------
freqs = np.fft.fftfreq(len(x), 1/fs)

# -----------------------------
# Step 5: Magnitude
# -----------------------------
magnitude = np.abs(X)

# -----------------------------
# Step 6: Plot frequency domain
# -----------------------------
plt.figure()

# Only plot positive frequencies
half = len(x) // 2
plt.plot(freqs[:half], magnitude[:half])

plt.title("Frequency Domain (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.show()