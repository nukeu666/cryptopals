from s1c3 import get_stat_array;
import os;

script_dir = os.path.dirname(__file__);
fo=open(os.path.join(script_dir,"4.txt"),"r");
data=fo.read().splitlines();
stat=map(lambda x:get_stat_array(x),data);
for x in stat:
    for e in x:
        if(e[0]>0.07):
            print(e);
    
