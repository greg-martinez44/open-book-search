#!/usr/bin/env bash

FILENAME=$1
PROD_DIR=openbooksearch
TEST_DIR=tests

echo "File name is $FILENAME"

readarray -td, a <<< "$FILENAME"; declare -p a;

echo $a