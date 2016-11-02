from base64 import b64decode;
from s1c2 import hex_xor;
from s1c1 import hex_u64;

LetterProbs=['.082','.015','.028','.043','.127','.022','.020','.061','.070','.002',
'.008','.040','.024','.067','.075','.019','.001','.060','.063','.091','.028',
'.010','.024','.002','.020','.001'];

def get_stat(x,s):
	s2="{:02x}".format(x)*(len(s)/2);
	a1=hex_xor(s,s2);
	a2=hex_u64(a1);
	out=b64decode(a2);
	if (all(ord(c) < 128 for c in out)):
		out_spaces=out.count(' ');
		out_filter=filter(lambda x:ord(x.lower())>97 and x.isalpha(),list(out));
		out_probs=map(lambda x:float(LetterProbs[ord(x.lower())-97]),out_filter);
		out_totals=(reduce(lambda x,y:x+y,out_probs,0.0)+.2*out_spaces)/len(out);
		return(out_totals,chr(x),out);

def get_stat_array(s):
	stat_array=filter(lambda x:x is not None,[get_stat(x,s) for x in range(0,127)]);
	if all(x is None for x in stat_array):
		return [(0,"")];
	else:
		return sorted(stat_array,key=lambda x:x[0],reverse=True);

if __name__=='__main__':
	#s="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
	s="1d4e1300330d1e1a090c004508621a";
	print(filter(lambda x:x[0]>0.0,get_stat_array(s)));

