#!/usr/bin/env python
import sys
import timeit
import random
import numpy
if __name__=="__main__":
    start=timeit.default_timer()
    n=10000000
    m=10000
    l=100
    a=numpy.array([0 for i in range(n) ])
    b=numpy.array([random.randint(0,m) for i in range(n) ])
    for i in range(l):
        a[random.randint(0,n)]=random.randint(1,m)
    for i in range(1000):
            a*b
    perior=timeit.default_timer()-start

    print perior
#340.0281231403351

