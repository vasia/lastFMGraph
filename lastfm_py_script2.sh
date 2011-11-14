#!/bin/bash

echo "*** Starting execution ***"
echo "Sample Size = 200"
echo "Estimating with k=2" >> out_200
python estimation.py ./output/sample_200 2 >> out_200
echo "Estimating with k=3" >> out_200
python estimation.py ./output/sample_200 3 >> out_200
echo "Estimating with k=4" >> out_200
python estimation.py ./output/sample_200 4 >> out_200
echo "Estimating with k=5" >> out_200
python estimation.py ./output/sample_200 5 >> out_200
echo "Estimating with k=10" >> out_200
python estimation.py ./output/sample_200 10 >> out_200
echo "Estimating with k=15" >> out_200
python estimation.py ./output/sample_200 15 >> out_200
echo "Estimating with k=20" >> out_200
python estimation.py ./output/sample_200 20 >> out_200

echo "Sample Size = 500"
echo "Estimating with k=2" >> out_500
python estimation.py ./output/sample_500 2 >> out_500
echo "Estimating with k=3" >> out_500
python estimation.py ./output/sample_500 3 >> out_500
echo "Estimating with k=4" >> out_500
python estimation.py ./output/sample_500 4 >> out_500
echo "Estimating with k=5" >> out_500
python estimation.py ./output/sample_500 5 >> out_500
echo "Estimating with k=10" >> out_500
python estimation.py ./output/sample_500 10 >> out_500
echo "Estimating with k=15" >> out_500
python estimation.py ./output/sample_500 15 >> out_500
echo "Estimating with k=20" >> out_500
python estimation.py ./output/sample_500 20 >> out_500

echo "Sample Size = 1000"
echo "Estimating with k=2" >> out_1000
python estimation.py ./output/sample_1000 2 >> out_1000
echo "Estimating with k=3" >> out_1000
python estimation.py ./output/sample_1000 3 >> out_1000
echo "Estimating with k=4" >> out_1000
python estimation.py ./output/sample_1000 4 >> out_1000
echo "Estimating with k=5" >> out_1000
python estimation.py ./output/sample_1000 5 >> out_1000
echo "Estimating with k=10" >> out_1000
python estimation.py ./output/sample_1000 10 >> out_1000
echo "Estimating with k=15" >> out_1000
python estimation.py ./output/sample_1000 15 >> out_1000
echo "Estimating with k=20" >> out_1000
python estimation.py ./output/sample_1000 20 >> out_1000

echo "Sample Size = 2000"
echo "Estimating with k=2" >> out_2000
python estimation.py ./output/sample_2000 2 >> out_2000
echo "Estimating with k=3" >> out_2000
python estimation.py ./output/sample_2000 3 >> out_2000
echo "Estimating with k=4" >> out_2000
python estimation.py ./output/sample_2000 4 >> out_2000
echo "Estimating with k=5" >> out_2000
python estimation.py ./output/sample_2000 5 >> out_2000
echo "Estimating with k=10" >> out_2000
python estimation.py ./output/sample_1000 10 >> out_2000
echo "Estimating with k=15" >> out_2000
python estimation.py ./output/sample_1000 15 >> out_2000
echo "Estimating with k=20" >> out_2000
python estimation.py ./output/sample_1000 20 >> out_2000

echo "Sample Size = 3000"
echo "Estimating with k=2" >> out_3000
python estimation.py ./output/sample_3000 2 >> out_3000
echo "Estimating with k=3" >> out_3000
python estimation.py ./output/sample_3000 3 >> out_3000
echo "Estimating with k=4" >> out_3000
python estimation.py ./output/sample_3000 4 >> out_3000
echo "Estimating with k=5" >> out_3000
python estimation.py ./output/sample_3000 5 >> out_3000
echo "Estimating with k=10" >> out_3000
python estimation.py ./output/sample_3000 10 >> out_3000
echo "Estimating with k=15" >> out_3000
python estimation.py ./output/sample_3000 15 >> out_3000
echo "Estimating with k=20" >> out_3000
python estimation.py ./output/sample_3000 20 >> out_3000

echo "Sample Size = 10000"
echo "Estimating with k=2" >> out_10000
python estimation.py ./output/sample_10000 2 >> out_10000
echo "Estimating with k=3" >> out_10000
python estimation.py ./output/sample_10000 3 >> out_10000
echo "Estimating with k=4" >> out_10000
python estimation.py ./output/sample_10000 4 >> out_10000
echo "Estimating with k=5" >> out_10000
python estimation.py ./output/sample_10000 5 >> out_10000
echo "Estimating with k=10" >> out_10000
python estimation.py ./output/sample_10000 10 >> out_10000
echo "Estimating with k=15" >> out_10000
python estimation.py ./output/sample_10000 15 >> out_10000
echo "Estimating with k=20" >> out_10000
python estimation.py ./output/sample_10000 20 >> out_10000
echo "Estimating with k=30" >> out_10000
python estimation.py ./output/sample_10000 30 >> out_10000
echo "Estimating with k=50" >> out_10000
python estimation.py ./output/sample_10000 50 >> out_10000

echo "Sample Size = 20000"
echo "Estimating with k=2" >> out_20000
python estimation.py ./output/sample_20000 2 >> out_20000
echo "Estimating with k=3" >> out_20000
python estimation.py ./output/sample_20000 3 >> out_20000
echo "Estimating with k=4" >> out_20000
python estimation.py ./output/sample_20000 4 >> out_20000
echo "Estimating with k=5" >> out_20000
python estimation.py ./output/sample_20000 5 >> out_20000
echo "Estimating with k=10" >> out_20000
python estimation.py ./output/sample_20000 10 >> out_20000
echo "Estimating with k=15" >> out_20000
python estimation.py ./output/sample_20000 15 >> out_20000
echo "Estimating with k=20" >> out_20000
python estimation.py ./output/sample_20000 20 >> out_20000
echo "Estimating with k=30" >> out_20000
python estimation.py ./output/sample_20000 30 >> out_20000
echo "Estimating with k=50" >> out_20000
python estimation.py ./output/sample_20000 50 >> out_20000

echo "Finished execution"
