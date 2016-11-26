import binascii;

def pkcs7_pad(st,l):
    padlen=int(l)-len(st);
    return("%s%s"%(st,(chr(padlen)*padlen)));

def pkcs7_hexpad(h,l):
    padlen=(int(l)-len(h))/2;
    return("%s%s"%(h,(str(padlen).zfill(2)*padlen)));

def pkcs7_key(s,key):
    padlen=len(s)+len(key)-len(s)%len(key)
    return pkcs7_pad(s,padlen)

if __name__ == '__main__':
    print(pkcs7_pad("YELLOW SUBMARINE",20));
    print(binascii.hexlify(pkcs7_pad("YELLOW SUBMARINE",20)));
    print(pkcs7_hexpad(binascii.hexlify("YELLOW SUBMARINE"),40));
    print(pkcs7_key("1234567890123456789012345","12345678"))