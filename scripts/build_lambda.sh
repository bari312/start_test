#!/bin/bash

cd src/lambda_handlers
for f in *.py; do
    fname=$(basename $f .py)
    zip -r ../../dist/${fname}.zip $f
done
