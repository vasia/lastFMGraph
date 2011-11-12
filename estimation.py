import urllib2
import random
import sys

sample = []
degree_sample = []

#reads the sample from a file
#and creates the two lists
#sample and degree_sample
#filename: the file containing the samples
#1st column is the username
#2nd column is the node degree
def read_samples(filename):
	f = open(filename, 'r')
	for line in f:
		elements = line.split()
		sample.append(elements[0])
		degree_sample.append(int(elements[1]))

## population estimation ##
#sample: usernames sample
#degree_sample: sample of node degrees
#k: thinning parameter
def thinning_estimation(k):
	pop_tot = 0
	for i in range(k):
		total_degree = 0
	        total_inverse_degree = 0
		sample_k = sample[i::k] #wow :D
	 	degree_k = degree_sample[i::k]
		collisions = collision_number(sample_k)
		for j in range(len(degree_k)):
			total_degree += degree_k[j]
			total_inverse_degree += 1/degree_k[j]
		else:
			population = (total_degree * total_inverse_degree)/ 2*collisions
			pop_tot += population
	return pop_tot/k

#Calculates the collisions in the sample
def collision_number(sample_k):
	collisions = 0
	for i in range(len(sample_k)-1):
		for j in range (i+1, len(sample_k)):
			if sample_k[i] == sample_k[j]:
				collisions += 1
	return collisions

if __name__ == '__main__':
	
	if len(sys.argv) != 3:
		print "\nUsage: " + sys.argv[0] + " inputFile k\n"
		sys.exit(0)

	#initialization
	sample = []
	degree_sample = []
	inputFile = sys.argv[1]
	k = int(sys.argv[2])
	#read the file
	read_samples(inputFile)
	#calculate the estimation
	estim_pop = thinning_estimation(k)
	#print results
	print estim_pop
