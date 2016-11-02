import binascii;
from s1c2 import hex_xor;

def enc_rep(s,key):
    a=binascii.hexlify(s);
    b=binascii.hexlify((key*(len(s)/len(key)+1))[:len(str(s))]);
    return hex_xor(a,b);

if __name__ == '__main__':
    s1="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal";
    print enc_rep(s1,"ICE");
    #0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
