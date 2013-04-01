#!/bin/bash

ls *.raw|awk '{
		for (i=1;i<=NF;i++){
			oldname=$i;
			sub(/.raw$/,"",$i);
			newname=$i;
			print "mv",oldname,newname;
		}
	}'| sh;

