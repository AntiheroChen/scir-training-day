#!/usr/bin/env python

class NGram(object):

    def __init__(self, n):
        # n is the order of n-gram language model
		self.n = n
		self.appeared=[]
		self.condition=[]

    # scan a sentence, extract the ngram and update their
    # frequence.
    #
    # @param    sentence    list{str}
    # @return   none
    def scan(self, sentence):
        # file your code here
		n=self.n
		for i in range(self.n+1,len(sentence)+1):
			#print '=',sentence[i-n-1:i]
			self.appeared.append(sentence[i-n-1:i])
		#print self.appeared
		for i in range(self.n,len(sentence)+1):
			#print '-',sentence[i-n:i]
			self.condition.append(sentence[i-n:i])
		#print self.condition

    # caluclate the ngram of the words
    #
    # @param    words       list{str}
    # @return   int         count of the ngram
    def ngram(self, words):
        # file your code here
		return self.appeared.count(words)



if __name__=="__main__":
	import sys
	try:
		fpi=open(sys.argv[1],"r")
	except IOError:
		print >> sys.stderr ,"failed to open file0."
	
	try:
		fpo_1=open(sys.argv[2],"w")
	except IOError:
		print >> sys.stderr,"failed to open file1."

	try:
		fpo_2=open(sys.argv[3],"w")
	except IOError:
		print >>sys.stderr,"failed to open file2."
	
	UNIGram=NGram(1);
	BIGram=NGram(2);
	for line in fpi: 
		#print line[:-1]
		#print line.split()
		UNIGram.scan(line.split())
		BIGram.scan(line.split())
	#print "c=", UNIGram.condition
	#print "go=",UNIGram.appeared
	UNIwords=[]
	for key in UNIGram.appeared:
		if not key in UNIwords:
			UNIwords.append(key)
			fpo_1.write(' '.join(key)+" "+str(UNIGram.ngram(key))+"\n")
	
	BIwords=[]
	for key in BIGram.appeared:
		if not key in BIwords:
			BIwords.append(key)
			fpo_2.write(' '.join(key)+" "+str(BIGram.ngram(key))+"\n")
