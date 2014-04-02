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

def find_maxfix_len():
    maxLen = 0
    maxRange = 10000
    for i in range(maxRange):
        cipher = sendMsg('a')
        maxLen = max(maxLen, len(cipher))
    print 'Maxfix is ' + str(maxLen)
    return maxLen


def find_key_len(res, maxFixLen):
    pattern = res [maxFixLen:maxFixLen + 10]
    i = maxFixLen + 1
    while i < len(res) - 10:
        if (pattern == res [i:i + 10]):
            return i - maxFixLen
        i += 1
    return None

def find_key():
    maxFixLen = find_maxfix_len()
    res = sendMsg('\x00' * maxFixLen * 4)
    key_len = find_key_len(res, maxFixLen)

    if key_len is None:
        print 'Can not find the key'
        return None
    else:
        print 'Key length is ' + str(key_len)
        r = (maxFixLen) % key_len
        r = key_len - r
        return res[maxFixLen+r:maxFixLen+key_len] + res[maxFixLen:maxFixLen+r]


key = find_key()
print 'Key is ' + key