#!/bin/bash

DAY=`date +%d`
YEAR=`date +%Y`
case "$1" in
  "test")
    ./day${DAY}/puzzle.py day${DAY}/test.txt ;;
  
  "create")
    mkdir "day${DAY}"
    touch "day${DAY}/puzzle.py"
    chmod +x "day${DAY}/puzzle.py"
    touch "day${DAY}/test.txt"
    ;;

  "debug")
    python -m pdb day${DAY}/puzzle.py day${DAY}/test.txt ;;
  *)
    curl -b cookiejar.txt https://adventofcode.com/${YEAR}/day/${DAY}/input | ./day${DAY}/puzzle.py
    ;;
esac
