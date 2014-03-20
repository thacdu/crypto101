'''
Enter a ciphertext as a hex string. Find plaintext if the length of key is one.
'''

from xor_key_len_1 import xor_key_len_one

def attack(cipher):
    for key in range(0, 127):
        print '[*]  ' + chr(key) + ':   ' + xor_key_len_one(cipher, chr(key))

if __name__ == '__main__':
    cipher = '1f030a080f1e'
    attack(cipher.decode('hex'))