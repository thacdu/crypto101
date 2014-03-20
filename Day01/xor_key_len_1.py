import sys

key = 'k'

def xor_key_len_one(msg, key):
    res = ''.join(chr(ord(m) ^ ord(key)) for m in msg)
    return res

if __name__ == '__main__':
    print xor_key_len_one(sys.argv[1], key).encode('hex')