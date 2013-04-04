#!/usr/bin/env python
import sys

if __name__=="__main__" :
    if len(sys.argv)!=2:
        exit(2)

    try :
        input=file(sys.argv[1],"r")
    except IOError:
        sys.stderr.wirte("Error: Cannot read file %s.",sys.argv[1])
        sys.ext(1)


    count={}
    file_text=input.readlines()

    for line in file_text:
        a=line.split()
        if len(a)<2:
            continue
        if count.has_key(a[0]):
            count[a[0]]+=1
        else :
            count[a[0]]=1

    for line in file_text:
        a=line.split()
        if len(a)<2:
            print 
            continue
        if count[a[0]]<5:
            for i in a[0]:
                if i.isdigit():
                    print "_Numeric_",
                    break
            else:
                if a[0].isupper():
                    print "_AllCapitals_",
                elif a[0][-1:].isupper():
                    print "_LastCapital_",
                else :
                    print "_RARE_",
            print a[1]
        else :
            print a[0],a[1]
