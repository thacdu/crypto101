###############################################
## Attack OTP when know about MSG and CIPHER ##
## Send msg to server and receive cipher     ##
###############################################

from socket import *

serverName = '127.0.0.1'
serverPort = 12345
clientSkt = socket(AF_INET, SOCK_DGRAM)

def sendMsg(msg):
    clientSkt.sendto(msg, (serverName, serverPort))
    cipher, serverAddr = clientSkt.recvfrom(2048)
    return cipher

def find_prefix_len():
    a = sendMsg('a')
    b = sendMsg('b')
    i = 0
    while a[i] == b[i]:
        i += 1

    return i

prefix_len = find_prefix_len()
print 'Prefix length: ' + str(prefix_len)

def find_key_len():
    msg = 'aaaaaaaaaa'
    pattern = sendMsg(msg)[prefix_len:prefix_len+10]
    i = 0

    while 1:
        i += 1
        msg += 'a'
        res = sendMsg(msg)[prefix_len+i:prefix_len+i+10]
        if res == pattern:
            return i

    return None


key_len = find_key_len()
print 'Key length: ' + str(key_len)

res = sendMsg('\x00' * key_len)

if key_len >= prefix_len:
    print 'Key: ' + res[key_len:prefix_len+key_len] + res[prefix_len:key_len]
else:
    r = prefix_len % key_len
    print 'Key: ' + res[prefix_len+key_len-r:prefix_len+key_len] + res[prefix_len:prefix_len+key_len-r]