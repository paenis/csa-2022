# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e))#.decode('latin-1').rstrip(PADDING)

def isprintable(s, codec='utf8'):
    try: s.decode(codec)
    except UnicodeDecodeError: return False
    else: return True

with open('words.txt','rb') as h:
    secrets = [line.strip().decode() for line in h.readlines()]

for secret in secrets:
    if secret[-1:] == "\n":
        print("Error, new line character at the end of the string. This will not match!")
    elif len(secret.encode('utf-8')) >= 32:
        print("Error, string too long. Must be less than 32 bytes.")
    else:
        # create a cipher object using the secret
        cipher = AES.new(secret.encode('utf-8') + ((BLOCK_SIZE - len(secret.encode('utf-8')) % BLOCK_SIZE) * PADDING).encode('utf-8'), AES.MODE_ECB)

        # decode the encoded string
        decoded = decode_aes(cipher, encrypted)

        if isprintable(decoded):
            print('Decoded: '+decoded.decode()+"\n")
            break
