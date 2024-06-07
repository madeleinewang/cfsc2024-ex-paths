#!/bin/bash
# Adds a term to the beginning of the PYTHONPATH shell variable.

echo Path was:
echo $PYTHONPATH
PYTHONPATH=$1:$PYTHONPATH
echo
echo Path is now:
echo $PYTHONPATH
