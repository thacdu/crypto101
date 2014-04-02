from xor_same_len import xor_same_len
from base64 import *
from keygen import key_gen
from random import randint


def binary(string):
    res = ''
    for st in string:
        res += bin(ord(st))[2:]
    return res

def hamming_distance(first, second):
    res = binary(xor_same_len(first, second))
    distance = 0
    for bit in res:
        distance += int(bit)
    return distance

def make_same_len(key, length):
    if len(key) > length:
        return key[:length]
    else:
        p = length / len(key)
        q = length % len(key)
        return key * p + key[:q]


alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))
alphabet.append(' ')
alphabet.append('!')
alphabet.append('.')
alphabet.append('?')

with open('ciphertexts') as file:
    ciphers = file.read().splitlines()
    for i in range(len(ciphers)):
        ciphers[i] = b64decode(ciphers[i])
        ciphers[i] = ciphers[i].lower()

    p = xor_same_len(ciphers[0][0], ciphers[1][0])
    print p

    m1_collection = []
    for m1 in alphabet:
        for m2 in alphabet:
            print xor_same_len(m1, m2)
            if xor_same_len(m1, m2) == p:
                m1_collection.append(m1)
    for msg in m1_collection:
        print msg