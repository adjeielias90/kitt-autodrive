import socketio
import eventlet
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image

sio = socketio.Server()
app = Flask(__name__) #'__main__'

@sio.on('telemetry')
def telemetry(sid, data):
  image = Image.open(BytesIO(base64.b64encode(data['image'])))




@sio.on('connect')
def connect(sid, environ):
  print('connected')
  send_control(0, 0)



def send_control(steering_angle, throttle):
  sio.emit('steer', data = {
    'steering_angle': steering_angle.__str__(),
    'throttle':throttle.__str__()
  })

if __name__ == '__main__':
  model = load_model('kitt.h5')
  app = socketio.Middleware(sio, app)
  eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
