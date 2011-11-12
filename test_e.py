import urllib2
import re
import random
import sys

#initialization
api_key = '1b4218629b50c1159e15a6b8285b90ba'

#sampling function
def sampling(user, limit, sample_size):
	sample = []
	degree_sample = []
	page = 1
	total_degree = 0
	total_inverse_degree = 0
	while sample_size > 0:
		command = "http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user="+user+"&limit="+str(limit)+"&page="+str(page)+"&api_key="+api_key
		data = urllib2.urlopen(command).read()      # XML format
		degree = int(re.search('total="(\d+)"', data).group(1))	#node degree
		#friends = re.findall("<name>(.*)</name>", data)
		#print degree       # number of friends of "rj"
		
		if degree != 0:	
			sample.append(user) #add user to the sample
			degree_sample.append(degree)	
			print degree
			#user = friends[int(random.uniform(0, min(degree, limit)))]	#random next user
			random_index = int(random.uniform(1, degree+1)) #since it is [a,b)
			print "random index is page= " + str(random_index)
			
			command = "http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user="+user+"&limit="+str(limit)+"&page="+str(random_index)+"&api_key="+api_key
			data = urllib2.urlopen(command).read()
			user = re.findall("<name>(.*)</name>", data)[0]  #assign the random friend to user, in order to be included in the next getfriend request
			print "po printohen users   "
			print user		
			sample_size = sample_size-1
		else:
			user = sample[-1] # go back to the last added user of the list
		
	return sample

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

def collision_number(sample):
	collisions = 0
	for i in range(len(sample)-1):
		for j in range (i+1, len(sample)):
			if sample[i] == sample[j]:
				collisions += 1
	return collisions
				
def thinning(sample,k):	
	return sample[::k]

if __name__ == '__main__':
	
	if len(sys.argv) < 4:
		print "\nUsage: " + sys.argv[0] + " limit sample_size k\n"
		sys.exit(0)

	limit = int(sys.argv[1])		#results per page
	sample_size = int(sys.argv[2])	#sample size
	k = int(sys.argv[3])			#thinning size
	user = "rj"		#username of starting user
	sample = []		#sampled nodes
	t_sample = []

	print user
	#add rj in the sample or not?

	#sampling
	sample = sampling(user, limit, sample_size)
	#thining
	t_sample = thinning(sample, k)
	collisions = collision_number(sample)
	print sample
	print "\n"
	print t_sample
	print "\n"
	print "No of collisions is " + str(collisions)
