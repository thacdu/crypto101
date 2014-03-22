from random import randint

def key_gen(key_len):
    key = ''
    for i in range(key_len):
        key += chr(randint(0, 255))
    return key