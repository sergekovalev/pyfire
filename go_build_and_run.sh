#!/bin/bash

echo "building..."
python src/main.py

echo "running..."
go run __dist__/main/main.go
