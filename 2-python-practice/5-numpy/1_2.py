#!/usr/bin/env python
import sys
import timeit
import random
import numpy
if __name__=="__main__":
    start=timeit.default_timer()
    a=numpy.array([random.randint(0,10000) for i in range(1000000) ])
    b=numpy.array([random.randint(0,10000) for i in range(1000000) ])
    for i in range(1000):
        c=a*b
    perior=timeit.default_timer()-start

    print perior
    print c
#10.713201046

