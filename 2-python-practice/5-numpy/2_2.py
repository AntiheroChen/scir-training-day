#!/usr/bin/env python
import sys
import timeit
import random
import numpy
if __name__=="__main__":
    start=timeit.default_timer()
    a=numpy.array([random.randint(0,10000) for i in range(100) ])
    b=numpy.array([random.randint(0,10000) for i in range(100) ])
    for i in range(1000):
        c=a*b
    perior=timeit.default_timer()-start

    print perior
#0.00346302986145


