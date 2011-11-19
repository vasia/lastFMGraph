import urllib2
import random
import sys

sample = []	#usernames
degree_sample = []	#node degrees

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
		if len(elements) > 1:
			sample.append(elements[0])
			degree_sample.append(int(elements[1]))
	f.close()

## population estimation ##
#sample: usernames sample
#degree_sample: sample of node degrees
#k: thinning parameter
def thinning_estimation(k):
	pop_tot = 0
	population = 0
	zeros = 0
	for i in range(k):
		total_degree = 0
	        total_inverse_degree = 0
		sample_k = sample[i::k] #wow :D
	 	degree_k = degree_sample[i::k]
		collisions = collision_number(sample_k)
		for j in range(len(degree_k)):
			total_degree += degree_k[j]
			total_inverse_degree += 1.0/degree_k[j]

		if collisions > 0:
			population = float((float(total_degree)*float(total_inverse_degree))/(2.0*collisions))
			pop_tot += population
		else:
			zeros += 1
	if k-zeros > 0:
		return_value = float(pop_tot)/float(k-zeros)
	else:
		return_value = -1
	return return_value

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
	inputFile = sys.argv[1]
	k = int(sys.argv[2])
	estim_pop = 0
	
	#read the file
	read_samples(inputFile)
	#calculate the estimation
	estim_pop = thinning_estimation(k)
	#print results
	print "Estimation = " + str(estim_pop)

