#!/usr/bin/env python
import sys

class Tagger(object):
    """The Tagger is used to tag the untaged data."""

    def __init__(self):
        self.tag={}

    def train(self,input_file):
        count={}
        file_text=input_file.readlines()
        for line in file_text:
            a=line.split()
            if count.has_key(a[2]):
                count[a[2]]+=int(a[0])
            else:
                count[a[2]]=int(a[0])

        for line in file_text:
            a=line.split()
            if len(a)<4:
                continue
            if a[1]!="WORDTAG":
                continue;
            #print a[2],float(a[0])/count[a[2]]
            if not self.tag.has_key(a[3]):
                self.tag[a[3]]=[a[2],float(a[0])/count[a[2]]]
            elif self.tag[a[3]][1] <float(a[0])/count[a[2]]:
                self.tag[a[3]]=[a[2],float(a[0])/count[a[2]]]

    def get_tag(self,x):
        if not self.tag.has_key(x):
        #    return "O"
            x="_RARE_"  
        return self.tag[x][0]


if __name__ == "__main__":
    
    if len(sys.argv)!=3:
        exit(2)

    try:
        input_file_1=file(sys.argv[1],"r")
    except IOError:
        sys.stderr.write("Error: Cannot read %s \n"%(argv[1]))
        exit(1)

    try:
        input_file_2=file(sys.argv[2],"r")
    except IOError:
        sys.stderr.write("Error: Cannot read %s \n"%(argv[2]))


    tagger=Tagger()
    tagger.train(input_file_1)
#    print tagger.get_tag("mRNA")
    for line in input_file_2:
        a=line.split()
        if len(a)<1:
            print 
        else :
            print a[0],tagger.get_tag(a[0])

