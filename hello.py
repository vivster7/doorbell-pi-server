from flask import Flask  
from flask import render_template  
import pygame
import time

app = Flask(__name__)  
  
@app.route('/')  
def hello(name=None):
  pygame.mixer.init()
  pygame.mixer.music.load('doorbell.mp3')
  pygame.mixer.music.play()
  time.sleep(20)

#   return render_template('hello.html') 

# @app.route('/ring', methods=['POST'])
# def ring():
#   if request.method == 'POST':
#     # Get the value id
#     id1 = request.form['id']
#     print "---Message is", id1
#   else:
#     id1 = None
#   return render_template('index.html', value=id1)
    
if __name__ == "__main__":  
  app.run('0.0.0.0') 

