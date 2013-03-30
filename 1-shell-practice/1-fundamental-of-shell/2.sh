#!/bin/bash

cur_path=$(pwd);
cur_time=$(date +%Y%m%d);
echo $cur_path;
echo $cur_time;

mkdir $cur_path"/tmp_"$cur_time;
