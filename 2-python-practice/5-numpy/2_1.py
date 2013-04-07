#!/usr/bin/env python
import sys
import timeit
import random

if __name__=="__main__":
    start=timeit.default_timer()
    n=10000000
    m=10000
    l=100
    a=[0 for i in range(n) ]
    b=[random.randint(0,m) for i in range(n) ]
    for i in range(l):
        a[random.randint(0,n)]=random.randint(1,m)
    for i in range(n):
        for j in range(n):
            a[j]*b[j]
    perior=timeit.default_timer()-start

    print perior
#3340.0381314733514

