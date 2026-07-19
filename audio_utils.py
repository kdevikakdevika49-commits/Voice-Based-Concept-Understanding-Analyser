import librosa
import numpy as np
import matplotlib.pyplot as plt


def extract_audio_features(audio_file):

    y, sr = librosa.load(audio_file, sr=None)

    duration = librosa.get_duration(y=y, sr=sr)

    rms = librosa.feature.rms(y=y)[0]

    avg_rms = float(np.mean(rms))

    return {
        "duration": round(duration, 2),
        "average_rms": round(avg_rms, 4)
    }


def create_waveform(audio_file):

    y, sr = librosa.load(audio_file, sr=None)

    fig, ax = plt.subplots(figsize=(10,3))

    ax.plot(y)

    ax.set_title("Audio Waveform")
    ax.set_xlabel("Samples")
    ax.set_ylabel("Amplitude")

    return fig