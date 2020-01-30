import sys
from flask import Flask, render_template, request
from numpy import loadtxt, asarray
from os import listdir, environ
from os.path import isfile, join
import random
import classification as classification
from threading import Thread

app = Flask(__name__)

@app.route('/process-file')
def run_neural_network():
  upload_path = "C:/wamp64/www/co600/Uploads"
  file_id = request.args.get('id')
  if not file_id:
    return 'File ID is required'
  file_path = join(upload_path, file_id) + '.csv'

  try:
    dataset = loadtxt(file_path, delimiter=',', skiprows=1, dtype=int)
  except OSError:
    print("File not found at: " + file_path)
    return 'File ID cannot be found'
  random.shuffle(dataset)

  input_variables = dataset[:,1:]
  output_variables = dataset[:,0]
  Thread(target=classification.run_neural_network, args=(file_id,input_variables,output_variables)).start()
  #classification.run_neural_network(file_id, input_variables, output_variables)
  return 'Processing started'

@app.route('/status')
def get_status():
  file_id = request.args.get('id')
  if not file_id:
    return 'File ID is required'
  try:
    with open('logs/' + file_id + '.log') as log:
      line = list(log)[-1]
      epoch = str(int(line.split(',')[0]) + 1)
      val_acc = line.split(',')[3]
      return 'Epocs Completed: ' + epoch + '/1500. Current Validation Accuracy: ' + val_acc
  except FileNotFoundError:
    return 'File ID could not be found'



if __name__ == '__main__':
  # This is used when running locally. Gunicorn is used to run the
  # application on Google App Engine. See entrypoint in app.yaml.
  app.run(host='127.0.0.1', port=8080, debug=True)