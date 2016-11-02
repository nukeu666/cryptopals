from Crypto.Cipher import AES;
import base64;
import os;

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__);
    fo=open(os.path.join(script_dir,"7.txt"),"r");
    data=fo.read();
    decryption_suite = AES.new('YELLOW SUBMARINE', AES.MODE_ECB);
    plain_text = decryption_suite.decrypt(base64.b64decode(data));
    print(plain_text);
    fo.close();
