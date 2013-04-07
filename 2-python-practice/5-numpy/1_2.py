#!/usr/bin/env python
import sys
import timeit
import random
import numpy
if __name__=="__main__":
    start=timeit.default_timer()
    n=10000000
    m=10000
    a=numpy.array([random.randint(0,m) for i in range(n) ])
    b=numpy.array([random.randint(0,m) for i in range(n) ])
    for i in range(1000):
        c=a*b
    perior=timeit.default_timer()-start

    print perior
    print c
#111.076565027

