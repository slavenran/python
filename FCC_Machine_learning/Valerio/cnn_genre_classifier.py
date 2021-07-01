import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras

DATA_PATH = "data.json"

def load_data(data_path):
    with open(data_path, "r") as fp:
        data = json.load(fp)

    # convert lists to numpy arrays
    x = np.array(data["mfcc"])
    y = np.array(data["labels"])

    return x, y

def prepare_dataset(test_size, validation_size):
    # load data
    x, y = load_data(DATA_PATH)

    # create the train/test split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)

    # create the train/validation split
    x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size=validation_size)

    # CNN expects 3d array (for each sample) -> (130, 13, 1)
    x_train = x_train[..., np.newaxis]  # 4d array -> (num_samples, 130, 30, 1)
    x_validation = x_validation[..., np.newaxis]
    x_test = x_test[..., np.newaxis]

    return x_train, x_validation, x_test, y_train, y_validation, y_test

def build_model(input_shape):
    # create model
    model = keras.Sequential()

    # 1st conv layer
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPool2D((3, 3), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization())

    # 2nd conv layer
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPool2D((3, 3), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization())

    # 3rd conv layer
    model.add(keras.layers.Conv2D(32, (2, 2), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPool2D((2, 2), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization())

    # flatten the output and feed it into dense layer
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dropout(0.3))

    # output layer
    model.add(keras.layers.Dense(10, activation='softmax'))

    return model

def predict(model, x, y):
    x = x[np.newaxis, ...]                              # x -> (130, 13, 1), needs to be (1, 130, 13, 1)

    # prediction = [[0.1, 0.2, ...]]
    prediction = model.predict(x)

    # extract index with max value
    predicted_index = np.argmax(prediction, axis=1)     # [4]
    print("Expected index: {}, Predicted index: {}".format(y, predicted_index))

if __name__ == "__main__":
    # create train, validation and test sets
    x_train, x_validation, x_test, y_train, y_validation, y_test = prepare_dataset(0.25, 0.2)

    # build the CNN network
    x_shape = x_train.shape                             # (num_samples, 130, 13, 1)
    input_shape = (x_shape[1], x_shape[2], x_shape[3])
    model = build_model(input_shape)

    # compile the network
    optimizer = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=optimizer,
                  loss="sparse_categorical_crossentropy",
                  metrics=['accuracy'])

    # train the CNN
    model.fit(x_train, y_train, validation_data=(x_validation, y_validation), batch_size=32, epochs=30)

    # evaluate the CNN on the test set
    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=1)
    print("Accuracy on test set is", test_accuracy)

    # make a prediction on a sample
    x = x_test[101]
    y = y_test[101]

    predict(model, x, y)