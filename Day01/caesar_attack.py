
cipher = 'MNUSBOHALSMNUSZIIFCMB'
cipher2 = 'owdugewlglzwzwdd'

def caesar_decrypt(alphabet, cipher, key):
    return ''.join(alphabet [(alphabet.index(i) - key) % 26] for i in cipher)

def caesar_attack(cipher):
    '''
    Attack Caesar Cipher
    '''

    alphabet = []
    [alphabet.append(chr(char)) for char in range(ord('a'), ord('z')+1)]

    for key in range(26):
        print str(key) + " " + caesar_decrypt(alphabet, cipher, key)

if __name__ == '__main__':
    caesar_attack(cipher.lower())
    caesar_attack(cipher2.lower())