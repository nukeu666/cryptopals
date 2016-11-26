from s2c3 import oracle,random_key
from s1c7 import aes_ecb_decrypt,aes_ecb_encrypt
import base64
from s2c1 import pkcs7_key

def make_enc_str(s1,s2,key):
    return(aes_ecb_encrypt(pkcs7_key(s1+s2,key),key))

def find_keylength(s2,key):
    enc_s2=make_enc_str("",s2,key)
    len=0
    appended_string=""
    while enc_s2 not in appended_string:
        len+=1
        appended_string=make_enc_str("a"*len,s2,key)
    return len

def make_hashes(keylen,key):
    return [aes_ecb_encrypt("a"*(keylen-1)+chr(x),key) for x in range(256)]

def decrypt_ecb(str,key):
    keylen=len(key)
    hashes=make_hashes(keylen,key)
    indexes=[hashes.index(aes_ecb_encrypt("a"*(keylen-1)+x,key)) for x in str]
    return ''.join([chr(x) for x in indexes])

if __name__ == '__main__':
    key=random_key(16)
    str=base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK");
    keylen=find_keylength(str,key)
    message=decrypt_ecb(str,key)
    print(message)