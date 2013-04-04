#!/usr/bin/env python
import sys
import math
class Tagger(object):
    """The Tagger is used to tag the untaged data."""

    def __init__(self):
        self.e_pro={}                               #the probability of emission.
        self.m_pro={}                               #the probability of transition.
        self.count={"O":0.0,"I-GENE":0.0}           #the count of O,I-GENE and N-gram.

    def train(self,file_text):
        count=self.count                            #give it a convient name
        key=()
        for line in file_text:                      
            a=line.split()
            if len(a)<2:                            #emptyline
                continue
            if a[1]=="WORDTAG":
                key=a[3]                            #count 1-gram
                count[a[2]]+=float(a[0])            #count O,I-GENE
            elif a[1]=="2-GRAM":
                key=(a[2],a[3])                     #count 2-gram
            elif a[1]=="3-GRAM":
                key=(a[2],a[3],a[4])                #count 3-gram
            if count.has_key(key):
                count[key]+=float(a[0])
            else:
                count[key]=float(a[0])

        #print "sizeof(count)=",count
        for line in file_text:
            a=line.split()
            if len(a)<4:                            #empty line
                continue
            if a[1]=="WORDTAG":                     #calculate the emission probability.
                self.e_pro[(a[2],a[3])]=float(a[0])/count[a[2]]
            elif a[1]=="3-GRAM":                    #calculate the transition probability.
                self.m_pro[(a[2],a[3],a[4])]=count[(a[2],a[3],a[4])]/count[(a[2],a[3])]


    def get_labeled_text(self,file_text):
        result=[]
        f={(-1,"*","*"):(0.0,"*")}                  #record state(position,x_i-1,x_i) about the (log(possibity),x_i-2) 
        seq=[]
        m_pro=self.m_pro
        e_pro=self.e_pro                            #give them a better name
        #print self.count
        for line in file_text:
            for element in line.split():            #read the element in the text and solve the _RARE_ words in advance.
                if self.count.has_key((element)) and self.count[(element)]>4.5:
                    seq.append(element)
                else:
                    seq.append("_RARE_")
        n=len(seq)                                  #take the number of words as n.
        #print "seq=",seq
        #print "n=",n
        #print 
        #print "m_pro=",m_pro
        #print e_pro[("O","E7")],
        #print e_pro[("I-GENE","E7")]
        #print
        #print "e_pro=",len(e_pro)
        #print seq[0:10]
        for i in range(n):                          #enumerate the position 
            #print "i=",i
            for key in m_pro:                       #enumerate the transition (x_i-2,x_i-1,x_i)

                if key[2]=="STOP":                  #there is no STOP!
                    continue

                tmp=0
                if f.has_key((i-1,key[0],key[1])):  #get the log(possibility)  of state(i-1,x_i-2,X_i-1)
                    tmp=f[(i-1,key[0],key[1])][0]
                else:
                    continue
                                                    #get the log(possibility) of emission
                if e_pro.has_key((key[2],seq[i])):
                    tmp+=math.log(e_pro[(key[2],seq[i])])
                else :
                    continue
                                                    #get the log(possibility) of transition
                tmp+=math.log(m_pro[key])
                #if i<50 and seq[i]=="E7":
                #    print "i=",i,"key=",key,"probability=",tmp
                                                    #record the state (position,x_i-1,x_i) about (log(possibity),x_i-2) and compare it.
                if (not f.has_key((i,key[1],key[2])) ) or f[(i,key[1],key[2])][0]<tmp:
                    f[(i,key[1],key[2])]=(tmp,key[0])

        ans=(-1,-2)
        for key in m_pro:
            if key[2]=="STOP" and f.has_key((n-1,key[0],key[1])):
                p=f[(n-1,key[0],key[1])][0]+math.log(m_pro[key])
                if len(ans)<3 or p>ans[0]:
                    ans=(p,key[0],key[1])

        x=ans[2]
        y=ans[1]
        #print "ans=",ans,y,x
        for i in range(n-1,-1,-1):
            result.append(x)
            #if i==43:
            #    print "x=",x,seq[i],result[i],len(result)
            z=f[(i,y,x)][1]
            x=y
            y=z

        #print "result=",result,"n="
        ret=[]
        i=0
        for line in file_text:
            for element in line.split():
                ret.append([element,result[n-1-i]])
                #if i==43:
                #    print "y=",element,result[n-1-i]
                i+=1
            ret.append("\n")

        return ret 


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
    tagger.train(input_file_1.readlines())
    print_text=tagger.get_labeled_text(input_file_2.readlines())

    for a in print_text:
        if len(a)<2:
            print 
        else: 
            print a[0],a[1],
#    print tagger.get_tag("mRNA")

