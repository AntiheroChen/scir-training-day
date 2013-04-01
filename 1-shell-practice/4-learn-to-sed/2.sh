#!/bin/bash

#awk '{$1="";$2="";print $0;}' 2.dat| sed "s/^''//g";
sed -e "s/^[^']*[']//" 2.dat|sed -e "s/'$//";

