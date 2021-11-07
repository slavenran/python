import librosa, librosa.display
from librosa.feature.spectral import mfcc
import matplotlib.pyplot as plt
import numpy as np

file = "C:\\Users\\Dzilaj Bilaj\\Desktop\\python\\FCC_Machine_learning\\Music_classification\\genres\\blues\\blues.00000.wav"

# waveform
data, sr = librosa.load(file) # data = sr * time (22050 * 30sec of data in data array)
librosa.display.waveplot(data, sr=sr)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

# fft -> spectrum
fft = np.fft.fft(data)
magnitude = np.abs(fft)
frequency = np.linspace(0 , sr, len(magnitude))

left_frequency = frequency[:int(len(frequency)/2)]
left_magnitude = magnitude[:int(len(frequency)/2)]

plt.plot(left_frequency, left_magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()

# stft -> spectogram
n_fft = 2048                    # no. of samples per STFT window (length of the windowed signal)
hop_length = 512                # number of audio samples between adjancent STFT columns

stft = librosa.core.stft(data, hop_length=hop_length, n_fft=n_fft)
spectogram = np.abs(stft)

log_spectogram = librosa.amplitude_to_db(spectogram)

librosa.display.specshow(log_spectogram, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar()
plt.show()

# MFCC
MFCCs = librosa.feature.mfcc(data, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)

librosa.display.specshow(MFCCs, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("MFCC")
plt.colorbar()
plt.show()