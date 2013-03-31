#!/bin/bash

awk '{count+=$2 ;print $1,$2,count}' 2.dat
