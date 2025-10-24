#!/bin/bash

# Based on here: https://leetcode.com/problems/word-frequency/description/
# Write a bash script to calculate the frequency of each word in a text file words.txt.
# For simplicity sake, you may assume:

# words.txt contains only lowercase characters and space ' ' characters.
# Each word must consist of lowercase characters only.
# Words are separated by one or more whitespace characters.
# Example:

# Assume that words.txt has the following content:

# the day is sunny the the
# the sunny is is
# Your script should output the following, sorted by descending frequency:

# the 4
# is 3
# sunny 2
# day 1

word_frecuency() {
    local filename="$1"
    cat "$filename" | tr ' ' '\n' | sort | uniq -c | sort -r
}

# Only execute if the script is run directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    word_frecuency files/001_word_frecuency.txt
fi
