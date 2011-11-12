
#population estimation
def thinning_estimation(sample,degree_sample,k):
	total_degree = 0
	total_inverse_degree = 0
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
	
	if len(sys.argv) != 3:
		print "\nUsage: " + sys.argv[0] + " sample_size k\n"
		sys.exit(0)

	sample_size = int(sys.argv[1])	#sample size
	k = int(sys.argv[2])			#thinning size
	user = "rj"		#username of starting user
	sample = []		#sampled nodes
	t_sample = []

	print user

	#sampling
	sample = sampling(user, sample_size)
	#thining
	t_sample = thinning(sample, k)
	collisions = collision_number(sample)
	print sample
	print "\n"
	print t_sample
	print "\n"
	print "No of collisions is " + str(collisions)
