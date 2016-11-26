import base64;
import binascii;
CODES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
inp = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
#expected=SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
def hex_u64old(inp):
	bin2 = ''.join(map(lambda x:((bin(int(x,16))+"")[2:]).zfill(4),"1"+inp));
	bin3 = ['{a:0<6}'.format(a=bin2[i:i+6]) for i in range(0,len(bin2),6)]
	bin4 = ''.join([CODES[int(i,2)] for i in bin3])+'{s:=<{l}}'.format(s="",l=(3-len(inp)%3));
	return bin4;

def hex_u64(inp):
	return base64.b64encode(binascii.unhexlify(inp));

if __name__=='__main__':
	print(hex_u64(inp));