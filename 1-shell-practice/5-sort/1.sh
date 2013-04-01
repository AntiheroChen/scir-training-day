#!/bin/bash

sort query_log.txt|uniq -c|sort -nr|awk '{
	if (NR<=100){print $2;}
	}'
