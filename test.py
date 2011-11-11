import urllib2
import re
import random
import sys

#initialization
api_key = '1b4218629b50c1159e15a6b8285b90ba'

#sampling function
def sampling(user, limit, sample_size):
	sample = []
	while sample_size > 0:
		command = "http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user="+user+"&limit="+str(limit)+"&page=1&api_key="+api_key
		data = urllib2.urlopen(command).read()      # XML format
		degree = int(re.search('total="(\d+)"', data).group(1))	#node degree
		friends = re.findall("<name>(.*)</name>", data)
		print degree       # number of friends of "rj"

		if degree != 0:	
			user = friends[int(random.uniform(0, min(degree, limit)))];	#random next user
			#print friends;      # first 'limit' friends
			print user;
			sample.append(user);	#add user to the sample	
			sample_size = sample_size-1

		#TODO: select another user in case degree = 0
	return sample

def thinning(sample, k):
	i = 0
	thin = []
	while i < len(sample):
		thin.append(sample[i])
		i = i + k
	return thin
	

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

	#print results
	print sample
	print "\n"
	print t_sample
