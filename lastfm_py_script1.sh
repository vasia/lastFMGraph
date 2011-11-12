#!/bin/bash

echo "*** Starting execution ***"
echo "Estimating with k=2"
python estimation.py sampleFile 2 >> out_k_2
echo "Estimating with k=5"
python estimation.py sampleFile 5 >> out_k_5
echo "Estimating with k=10"
python estimation.py sampleFile 10 >> out_k_10
echo "Estimating with k=20"
python estimation.py sampleFile 20 >> out_k_20
echo "Estimating with k=50"
python estimation.py sampleFile 50 >> out_k_50
