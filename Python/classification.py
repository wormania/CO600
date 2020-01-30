from numpy import loadtxt, asarray
from os import listdir, environ
from os.path import isfile, join
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, CSVLogger
environ["CUDA_VISIBLE_DEVICES"]="-1"

def run_neural_network(file_id, input_variables, output_variables):
  model = Sequential()
  model.add(Dense(50, input_dim=6, activation='relu'))
  model.add(Dense(50, activation='relu'))
  model.add(Dense(50, activation='relu'))
  model.add(Dense(50, activation='relu'))
  model.add(Dense(25, activation='relu'))
  model.add(Dense(1, activation='sigmoid'))

  model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

  model_location = './models/output.h5'
  callbacks = [EarlyStopping(monitor='val_accuracy', patience=1500),
              ModelCheckpoint(model_location, save_best_only=True, save_weights_only=False),
              CSVLogger('logs/' + file_id + '.log')]

  model.fit(input_variables, output_variables, epochs=1500, batch_size=10, validation_split=0.5, callbacks=callbacks)