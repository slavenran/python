import os
import librosa
import math
import json
import random

# Script for preprocessing music dictionary into single json file ready for training

DATASET_PATH = "../genres"
JSON_PATH = "../music_data/manual_data.json"

SAMPLE_RATE = 22050
DURATION = 30
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION

def save_mfcc(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=10):
    # dictionary to store data
    data_lib = {
        "mapping": [],
        "mfcc": [],
        "labels": [],
        "mfccTest": [],
        "labelsTest": []
    }

    num_samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length)

    # loop through all the genres
    for i, (dirpath, _, filenames) in enumerate(os.walk(dataset_path)):
        # ensure that we're not at the root level
        if dirpath is not dataset_path:
            # save semantic label
            dirpath_components = os.path.split(dirpath)
            semantic_label = dirpath_components[-1]
            data_lib["mapping"].append(semantic_label)
            print("\nProcessing", semantic_label)

            # generate random numbers to move 20% of dataset in test data
            random_numbers = random.sample(range(0, 10), 2)

            # process files for a specific genre
            for i_file, (f) in enumerate(filenames):
                mapping_mfcc = "mfcc"
                mapping_label = "labels"

                if i_file % 10 in random_numbers:
                    mapping_mfcc = "mfccTest"
                    mapping_label = "labelsTest"

                # load audio file
                file_path = os.path.join(dirpath, f)
                data, sr = librosa.load(file_path)

                # process segments extracting mfcc and storing data
                for s in range(num_segments):
                    start_sample = num_samples_per_segment * s
                    end_sample = start_sample + num_samples_per_segment

                    mfcc = librosa.feature.mfcc(data[start_sample:end_sample], sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)
                    mfcc = mfcc.T

                    # store MFCC for segment if it has expected length
                    if len(mfcc) == expected_num_mfcc_vectors_per_segment:
                        data_lib[mapping_mfcc].append(mfcc.tolist())
                        data_lib[mapping_label].append(i-1)
                        print("{}, segment:{}".format(file_path, s))
    
    with open(json_path, "w") as fp:
        json.dump(data_lib, fp, indent=4)

if __name__ == "__main__":
    save_mfcc(DATASET_PATH, JSON_PATH, num_segments=10)