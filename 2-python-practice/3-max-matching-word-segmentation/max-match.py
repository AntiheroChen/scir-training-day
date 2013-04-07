#!/usr/bin/env python
import cPickle as pickle
import sys

def max_match_segment( line, dic ):
    # write your code here
    line=unicode(line,"utf-8")
    ret=[]
    beg=0 
    #print line
    #print line[0],len(line)
    while beg<len(line):
        for i in range(len(line),beg,-1):
            key=line[beg:i].encode("utf-8")
            if key in dic:
                ret.append(key)
                beg=i
                break
        else:
            key=line[beg:beg+1].encode("utf-8")
            ret.append(key)
            beg+=1
    return ret


if __name__=="__main__":

    try:
        fpi=open(sys.argv[1], "r")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    try:
        fdic=open(sys.argv[2],"r")
        dic = pickle.load(fdic)
    except:
        print >> sys.stderr, "failed to load dict"
        sys.exit(1)

    #for key in dic:
    #    print key
    for line in fpi:
        #line.decode("utf-8")
        #print "\t".join(line.strip().split() )
        #for word in line:
        #    print word,
        #print
        #print line.decode("utf-8")
        print  "\t".join(max_match_segment(line.strip(), dic)) 

