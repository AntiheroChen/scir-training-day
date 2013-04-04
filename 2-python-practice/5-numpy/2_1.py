#!/usr/bin/env python
import sys
import timeit
import random

if __name__=="__main__":
    start=timeit.default_timer()
    a=[random.randint(0,10000) for i in range(100) ]
    b=[random.randint(0,10000) for i in range(100) ]
    for i in range(1000):
        for j in range(100):
            a[j]*b[j]
    perior=timeit.default_timer()-start

    print perior
#0.0281231403351

