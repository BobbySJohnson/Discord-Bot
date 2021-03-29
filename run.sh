#!/bin/bash

timeout $1 python3 main.py
sleep 10
timeout $1 python3 bbma.py

exit 0
