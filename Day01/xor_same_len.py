import sys

def xor_same_len(msg1, msg2, length):
    res = ''.join(chr(ord(msg1[i]) ^ ord(msg2[i])) for i in range(length))
    return res

if __name__ == '__main__':
    print "Hex of the result: " + xor_same_len(sys.argv[1], sys.argv[2], len(sys.argv[1])).encode('hex')

