import configparser
import socket
import time

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
sock.send("CAP REQ :twitch.tv/tags {}\n".encode("utf-8"))


while (True) :
  resp = sock.recv(2048).decode('utf-8')

  print (resp)
  time.sleep(1)