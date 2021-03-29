#!/bin/bash

timeout $1 python3 bbma.py &
sleep 10
timeout $1 python3 main.py

exit 0
