import os;
import collections;

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__);
    fo=open(os.path.join(script_dir,"8.txt"),"r");
    data=fo.read().splitlines();
    for line in data:
        splits = [line[2*i:2*i+16] for i in xrange(len(line)/2)];
        counts = [(item,count) for item, count in collections.Counter(splits).items() if count > 1];
        if counts:
            print(line);
            print(counts);
    fo.close();
