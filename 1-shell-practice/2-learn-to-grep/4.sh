#!/bin/bash

#temp=$(grep "Total:" 4.dat);
#echo $temp;
#echo "---";

grep "Total:" 4.dat | while read line
do
	P1=${line#*P=};
	P=${P1%%(*};
	R2=${line#*R=};
	R=${P1%%(*};
	F=${line#*F=};
	P=`echo $P |awk '{printf("%.2f",$1)}'`
	R=`echo $R |awk '{printf("%.2f",$1)}'`
	F=`echo $F |awk '{printf("%.2f",$1)}'`
	echo P=$P R=$R F=$F;
done
#echo $temp;
