import numpy as np
import matplotlib.pyplot as plt
import cv2

# # Step 1: Create the signal
# fs = 100  # Sampling frequency (Hz)
# t = np.linspace(0, 1, fs, endpoint=False)

# # Signal: 2 Hz + 5 Hz (this is a vector)
# x = np.sin(2*np.pi*2*t) + np.sin(2*np.pi*5*t)

# # Step 2: Plot time domain
# plt.figure()
# plt.plot(t, x)
# plt.title("Time Domain Signal")
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude")

# # Step 3: Apply FFT (frequency space, each elem is a complex number)
# X = np.fft.fft(x)

# # Step 4: Get frequencies
# freqs = np.fft.fftfreq(len(x), 1/fs)

# # Step 5: Magnitude (converts from complex to size, to tell what frequencies you got)
# magnitude = np.abs(X)
# print(freqs,magnitude.shape)

# # Step 6: Plot frequency domain
# plt.figure()
# half = len(x) // 2 # Only plot positive frequencies
# plt.plot(freqs[:half], magnitude[:half])
# plt.title("Frequency Domain (FFT)")
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude")
# plt.show()


##############################################################################

img = cv2.imread('home_bot.jpg', 0)

# Apply FFT
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Magnitude spectrum
magnitude = 20 * np.log(np.abs(fshift))

plt.imshow(magnitude, cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()