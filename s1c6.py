import binascii;
from base64 import b64decode;
from s1c2 import hex_xor;
from s1c3 import get_stat_array;
from s1c5 import enc_rep;
import os;

def hamming(s1,s2):
    return hamming_hex(binascii.hexlify(s1),binascii.hexlify(s2));
    
def hamming_hex(h1,h2):
    diff_bin=bin(int(hex_xor(h1,h2),16))[2:];
    ham=reduce(lambda sum,e:sum+int(e),list(diff_bin),0);
    return ham
#print(hamming("this is a test","wokka wokka!!!"));#37

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__);
    fo=open(os.path.join(script_dir,"6.txt"),"r");
    raw_data=fo.read();
    data=binascii.hexlify(b64decode(raw_data));
    fo.close();
    
    hams=[(hamming_hex(data[0:10*size],data[size:10*2*size])/float(10*size),size) for size in range(2,80,2)];
    hams=sorted(hams,key=lambda x:x[0]);
    for x in hams[:4]:
        print("Normalized hamming:%f\nKeylen:%i"%(float(x[0]),x[1]/2)); #keylengths are already doubled for hex
        keylen=x[1];
        transposed=[[data[i+j:i+j+2] for j in range(0,len(data),keylen)]for i in range(0,keylen,2)]
        transposed_joined=map(lambda x:''.join(x),transposed);
        make_key=[get_stat_array(transposed_joined[i])[0][1] for i in range(len(transposed_joined))]
        key=''.join(make_key);
        print("Key:",key);
        print(binascii.unhexlify(enc_rep(b64decode(raw_data),key)));

