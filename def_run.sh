#!/bin/bash
# source: http://stackoverflow.com/questions/9023164/in-bash-how-can-i-run-multiple-infinitely-running-commands-and-cancel-them-all

# Init
source ./env/Scripts/activate

# Watch
python run.py &
PIDS[0]=$!

trap "kill ${PIDS[*]}; deactivate" SIGINT

wait