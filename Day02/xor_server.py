'''
Find key of OTP when key is reused
'''
from xor_same_len import xor_same_len
from random import randint
from keygen import key_gen
from socket import *

key = key_gen(randint(20, 100))
prefix = key_gen(randint(10, 20))
suffix = key_gen(randint(10, 20))


print 'Key: ' + key.encode('hex')

serverPort = 12345
servSocket = socket(AF_INET, SOCK_DGRAM)
servSocket.bind(('', serverPort))
print 'OTP server is running...'

def make_same_len(key, length):
    if len(key) > length:
        return key[:length]
    else:
        p = length / len(key)
        q = length % len(key)
        return key * p + key[:q]

while 1:
    msg, clientAddr = servSocket.recvfrom(2048)
    msg = prefix + msg + suffix
    cipher = xor_same_len(msg, make_same_len(key, len(msg)))
    servSocket.sendto(cipher.encode('hex'), clientAddr)