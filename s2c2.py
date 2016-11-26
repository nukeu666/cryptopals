import os
import binascii
from base64 import b64decode
from s1c2 import hex_xor
from s1c7 import aes_ecb_decrypt,aes_ecb_encrypt

def encrypt_cbc(data,iv,key):
    enc_data=[]
    keylen=len(key)
    xor_with=binascii.hexlify(iv)
    for block in [data[i:i+keylen] for i in range(0,len(data),keylen)]:
        xored=hex_xor(binascii.hexlify(block),xor_with)
        enc_aes=aes_ecb_encrypt(binascii.unhexlify(xored),key)
        enc_data.append(''.join(enc_aes))
        xor_with=binascii.hexlify(enc_aes)
    return ''.join(enc_data)

def decrypt_cbc(enc_data,iv,key):
    dec_data=[]
    keylen=len(key)
    xor_with=binascii.hexlify(iv)
    for block in [enc_data[i:i+keylen] for i in range(0,len(enc_data),keylen)]:
        aes_data_h=binascii.hexlify(aes_ecb_decrypt(block,key))
        dec_data.append(''.join(hex_xor(aes_data_h,xor_with)))
        xor_with=binascii.hexlify(block)
    return (binascii.unhexlify(''.join(dec_data)))

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    fo=open(os.path.join(script_dir,"10.txt"),"r")
    raw_data=b64decode(fo.read()) 
    key="YELLOW SUBMARINE"
    iv=binascii.unhexlify("00"*len(key))
    
    data="Decrypting with the incorrect IV caucses the first block of plaintext to be corrupt but subsequent plaintext blocks will be correct. This is because each block is XORed with the            ciphertext of the previous block, not the plaintext, so one does not need to decrypt the previous block before using it as the IV for the decryption of the current one"
    dec=decrypt_cbc(encrypt_cbc(data,iv,key),iv,key)
    #dec=decrypt_cbc(raw_data,iv,key)
    print(dec)
