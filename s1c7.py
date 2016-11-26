from Crypto.Cipher import AES
import base64
import os

def aes_ecb_decrypt(data,key):
    decryption_suite = AES.new(key, AES.MODE_ECB)
    plain_text = decryption_suite.decrypt(data)
    return(plain_text)

def aes_ecb_encrypt(data,key):
    decryption_suite = AES.new(key, AES.MODE_ECB)
    enc_text = decryption_suite.encrypt(data)
    return(enc_text)

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    fo=open(os.path.join(script_dir,"7.txt"),"r")
    data=fo.read()
    print(aes_ecb_decrypt(base64.b64decode(data),"YELLOW SUBMARINE"))
    fo.close()
