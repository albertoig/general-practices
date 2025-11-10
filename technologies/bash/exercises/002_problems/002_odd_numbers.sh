#!/bin/bash

# Your task is to use for loops to display only odd natural numbers from 1 to 99
# Output Format Example: 

#1
#3
#5
#.
#.
#.
#.
#.
#99  

for number in {1..99..2}; do
    echo "$number"
done
