#!/bin/bash
# set -x
today=`date +%Y-%m-%d`
python3 daily.py data/yesterday/$today.csv

