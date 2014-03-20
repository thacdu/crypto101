from base64 import b64encode, b64decode
import sys

def main(bystream):
    '''
    Input a bystream, convert to hex and base64
    '''

    ###
    # Estimate hex encode bystream byte by byte
    ###
    res = ''
    for char in bystream:
        res += str(hex(ord(char))[-2:])
    # can do by decode('hex')

    print res
    print bystream.encode('hex') # the same as above
    print b64encode(bystream)


if __name__ == '__main__':
    main(sys.argv[1])
