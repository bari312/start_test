#!/bin/bash

cd src/lambda_handlers
mkdir -p ../../dist
for f in *.py; do
    fname=$(basename $f .py)
    zip -r ../../dist/${fname}.zip $f
done
