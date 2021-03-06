import urllib2
import re
import random
import sys
import datetime



#initialization
api_key = '1b4218629b50c1159e15a6b8285b90ba'
COMM = 'http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user='

#sampling function
def sampling(user, sample_size):
	page = 1
	now = datetime.datetime.now()
	f = open('/home/hinata/PythonProjects/lastFMGraph/output/sample_' + str(sample_size), 'a')
	last_sampled_user = user
	while sample_size > 0:
		command = COMM+user+"&limit=1&page="+str(page)+"&api_key="+api_key	#limit=1 always
		data = urllib2.urlopen(command).read()      # XML format
		degree = int(re.search('total="(\d+)"', data).group(1))	#node degree
		
		if degree != 0:	
			line = user + " " + str(degree) + "\n" 
			f.write(line) #add user and degree to the sample file
			last_sampled_user = user
			random_index = int(random.uniform(1, degree+1)) #since it is [a,b)
			command = COMM+user+"&limit=1&page="+str(random_index)+"&api_key="+api_key
			data = urllib2.urlopen(command).read()
			user = re.findall("<name>(.*)</name>", data)[0]  #assign the random friend to user, in order to be included in the next getfriend request
			sample_size = sample_size-1
		else:
			user = last_sampled_user # go back to the last added user of the list
	f.close()	
	#return sample
				
if __name__ == '__main__':
	
	if len(sys.argv) != 3:
		print "\nUsage: " + sys.argv[0] + " sample_size user\n"
		sys.exit(0)

	sample_size = int(sys.argv[1])	#sample size
	user = sys.argv[2]	#user
	sample = []		#sampled nodes
	t_sample = []

	
	#sampling
	sampling(user, sample_size)
	
