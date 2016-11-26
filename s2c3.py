from binascii import hexlify,unhexlify
import random
import os
import sets
from s1c7 import aes_ecb_decrypt,aes_ecb_encrypt
from s2c2 import encrypt_cbc,decrypt_cbc
from s2c1 import pkcs7_key

def random_key(len):
    key=b''
    for _ in range(len):
        key+=chr(random.randrange(0,256))
    return key

def oracle(data): #ECB=true, CBC=false
    chunksize=16
    all_repeats=[0]
    for offset in range(0,5):
        chunks=sets.Set()
        repeats=0
        for chunk in [data[i+offset:i+offset+chunksize] for i in range(0,len(data),chunksize)]:
            if chunk in chunks:
                return True #if duplicate chunk found then ECB
            else:
                chunks.add(chunk)
        all_repeats.append(repeats)
    return False #(max(all_repeats)>0) #CBC

if __name__ == '__main__':
    key=random_key(16)
    iv=random_key(16)
    mode=random.randint(0,1)
    pre_buffer=random_key(random.randrange(5))
    post_buffer=random_key(random.randrange(5))
    
    script_dir = os.path.dirname(__file__)
    fo=open(os.path.join(script_dir,"asciidata.txt"),"r")
    raw_data=fo.read()
    fo.close()
    rand_data=pkcs7_key(str(pre_buffer)+raw_data+str(post_buffer),key)

    if mode:#1
        enc_data=aes_ecb_encrypt(rand_data,key)
    else:#0
        enc_data=encrypt_cbc(rand_data,iv,key)
    print(key,mode,oracle(enc_data))