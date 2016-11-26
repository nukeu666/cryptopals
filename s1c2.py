def hex_xor(s1,s2):
	#print(s1,s2)
	return hex(int(bin(int(s1,16))[2:],2)^int(bin(int(s2,16))[2:],2))[2:-1].zfill(len(s1));

if __name__=='__main__':
	s1="1c0111001f010100061a024b53535009181c"
	s2="686974207468652062756c6c277320657965"
	#expected=746865206b696420646f6e277420706c6179
	print(hex_xor(s1,s2))
	