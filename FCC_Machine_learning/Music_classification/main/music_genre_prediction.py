import math
import operator
import librosa
import numpy as np
from tensorflow.keras.models import load_model

# Genres
genres = [
        "blues",
        "classical",
        "country",
        "disco",
        "hiphop",
        "jazz",
        "metal",
        "pop",
        "reggae",
        "rock"
    ]

# Filepath to model
model_filepath = "../models/full_model"

# load the model
model = load_model(model_filepath, compile=True)

def predict(file_path):
    # load a custom song
    file = file_path
    data, sr = librosa.load(file) # data = sr * time (ex. 22050 * 30sec of data in data array)

    # calculate the track duration in sec
    track_duration = math.floor(data.shape[0]/sr)

    # data for preprocessing the file (must be same as the trained files)
    NUM_SEGMENT = track_duration//3     # cuts the track to segments of 3 seconds
    N_MFCC=13
    N_FFT=2048                          # no. of samples per STFT window (length of the windowed signal)
    HOP_LENGTH=512                      # number of audio samples between adjancent STFT columns
    NUM_SAMPLES_PER_SEGMENT = 66150

    # processing file for prediction
    prediction_mfcc = []
    for s in range(NUM_SEGMENT):
        start_sample = NUM_SAMPLES_PER_SEGMENT * s
        end_sample = start_sample + NUM_SAMPLES_PER_SEGMENT

        mfcc = librosa.feature.mfcc(data[start_sample:end_sample], sr=sr, n_mfcc=N_MFCC, n_fft=N_FFT, hop_length=HOP_LENGTH)
        mfcc = mfcc.T

        # store MFCC for segment
        prediction_mfcc.append(mfcc.tolist())
    prediction_mfcc = np.array(prediction_mfcc)

    # dict for storing multiple genre values with count
    predicted_values = {}
    for i in range(prediction_mfcc.shape[0]):
        prediction = model.predict(prediction_mfcc[i][np.newaxis, ..., np.newaxis])
        predicted_index = np.argmax(prediction)
        predicted_values[genres[predicted_index]] = predicted_values.get(genres[predicted_index], 0) + 1

    # pulling the genre with max occurences in dict and printing the predicted value
    predicted_genre = max(predicted_values.items(), key=operator.itemgetter(1))[0]
    print(f"Your song is predicted to be of a {predicted_genre} genre.")
    return predicted_genre