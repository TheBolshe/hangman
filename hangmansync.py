import configparser
import socket
import time
import re

config = configparser.ConfigParser()
config.read('twitch.cfg')

server = 'irc.chat.twitch.tv'
port = 6667
nickname = config['CREDENTIALS']['username']
token = config['CREDENTIALS']['token']
channel = '#thebolshe'

sock = socket.socket()

sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))
sock.send("CAP REQ :twitch.tv/tags\n".encode("utf-8"))

resp = sock.recv(2048).decode('utf-8')


word = 'abstrait'

def createBoolList(w) :
  list = []
  for c in w:
    list.append(False)
  return list

boolList = createBoolList(word)
tries = 7

triedLetters = []


while (True) :
  resp = sock.recv(2048).decode('utf-8')
  if resp.startswith('PING'):
    sock.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))
    print('pong sent')
  else:
    [tags, message] = re.split(':', resp, 1)
    
    print(message)
  time.sleep(0.1)