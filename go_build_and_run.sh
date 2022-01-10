#!/bin/bash

echo "building...\n"
python src/main.py

echo "running...\n"
go run __dist__/main/main.go
