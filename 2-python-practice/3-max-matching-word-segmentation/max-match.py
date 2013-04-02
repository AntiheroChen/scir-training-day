#!/usr/bin/env python
import cPickle as pickle
import sys

def max_match_segment( line, dic ):
    # write your code here
    ret=[]
    last=len(line)-1 # There is a enter notation in the end of the sentence.
    while last>0:
        for i in range(0,last):
            if line[i:last] in dic:
                ret.append(line[i:last])
                last=i
                break
        else:
            return False
    return ret


if __name__=="__main__":

    try:
        fpi=open(sys.argv[1], "r")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    try:
        dic = pickle.load(sys.argv[2])
    except:
        print >> sys.stderr, "failed to load dict"
        sys.exit(1)

    for line in fpi:
        print "\t".join( max_match_segment(line.strip(), dic) )

