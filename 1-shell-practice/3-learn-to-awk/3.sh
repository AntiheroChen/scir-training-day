#!/bin/bash

awk  '{for(i=1;i<=NF;i++){sub(/_[a-zA-Z]*/,"",$i)}OFS=""; print $0}' 3.dat;

