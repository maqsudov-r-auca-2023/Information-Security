#!/bin/bash
if [[ $# -ne 2 ]]; then
    echo "Usage: $0 <file> <word>"
    exit 1
fi

file=$1
word=$2

count=$(grep -o -i "\b$word\b" "$file" | wc -l)
echo "The word '$word' appears $count times in $file."
