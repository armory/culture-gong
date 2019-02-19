from slackclient import SlackClient
import os
import time
from servosix import ServoSix
import sys

class GongBerry:
    def __init__(self, numRatches):
        if numRatches < 1 or numRatches > 20:
            raise ValueError('Needs to be between 1 and 20')

        self.numRatches = numRatches
        self.ss = ServoSix()
        self.period = 0.7

    def open(self):
        self.ss.set_servo(2, 170)
        time.sleep(self.period)
        self.ss.set_servo(1, 0)

    def close(self):
        self.ss.set_servo(2, 150)
        self.ss.set_servo(1, 90)
    
    def rat(self):
        self.ss.set_servo(2, 150)
        time.sleep(self.period)
        self.ss.set_servo(2, 50)
        time.sleep(self.period)

    def doit(self):
        try:
           self.close()
           for x in range(self.numRatches):
               self.rat()
           self.open()
        finally:
            self.ss.cleanup()
            time.sleep(1)

slack_token = os.environ['SLACK_TOKEN']
sc = SlackClient(slack_token)

if sc.rtm_connect(with_team_state=False):
  while True:
    message = sc.rtm_read()
    if message:
      for item in message:
        if 'text' in item.keys() and ':gong:' in item['text']:
          try:
            score = item['text'].count(':gong:')
            GongBerry(6+score).doit()
          except:
            pass
else:
  print 'Connection Failed'
