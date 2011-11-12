import urllib2
import random
import sys

#reads the sample from a file
#and creates the two lists
#sample and degree_sample
#filename: the file containing the samples
#1st column is the username
#2nd column is the node degree
def read_samples(filename, sample, degree_sample):
	f = open(filename, 'r')
	for line in f:
		elements = line.split()
		sample.append(elements[0])
		degree_sample.append(int(elements[1]))
	print sample
	print degree_sample

## population estimation ##
#sample: usernames sample
#degree_sample: sample of node degrees
#k: thinning parameter
def thinning_estimation(sample,degree_sample,k):
	pop_total = 0
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
def collision_number(sample):
	collisions = 0
	for i in range(len(sample)-1):
		for j in range (i+1, len(sample)):
			if sample[i] == sample[j]:
				collisions += 1
	return collisions

if __name__ == '__main__':
	
	if len(sys.argv) != 2:
		print "\nUsage: " + sys.argv[0] + " inputFile\n"

	sample = []
	degree_sample = []
	read_samples(sys.argv[1], sample, degree_sample)	
