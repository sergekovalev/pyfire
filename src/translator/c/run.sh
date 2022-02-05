#!/bin/bash

DIST="build"

mkdir $DIST

cd $DIST
cmake ..
make -j$(nproc)

./maind

#if [ "$1" == "-r" ]; then
#  ./maind "$@"
#fi

