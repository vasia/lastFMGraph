#!/bin/bash

echo "*** Starting execution of sampling ***"
echo "Sampling with sample_size = 1000"
python sampling.py 1000
echo "Sampling with sample_size = 2000"
python sampling.py 2000
echo "Sampling with sample_size = 5000"
python sampling.py 3000
echo "Sampling with sample_size = 10000"
python sampling.py 10000
echo "Sampling with sample_size = 20000"
python sampling.py 20000
echo "*** Finished execution of sampling ***"

