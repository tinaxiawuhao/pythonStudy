import torch
import torchaudio
import matplotlib.pyplot as plt


torchaudio.set_audio_backend("soundfile")
filename = "./audio/2.mp3"
waveform, sample_rate = torchaudio.load(filename)
print("Shape of waveform: {}".format(waveform.size()))
print("Sample rate of waveform: {}".format(sample_rate))
plt.figure()
plt.plot(waveform.t().numpy())

plt.title("Waveform")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

# 显示图像
plt.show()