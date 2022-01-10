#!/bin/bash

echo "building...\n"
python src/main.py file samples/code.py

echo "running...\n"
go run __dist__/main/main.go
