import urllib2
import re

#initialization
api_key = '1b4218629b50c1159e15a6b8285b90ba'
sample_size = 0
user = "rj"

print user

#sampling
while sample_size < 10:
	command = "http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user="+user+"&limit=10&page=1&api_key="+api_key
	data = urllib2.urlopen(command).read()      # XML format
	degree = int(re.search('total="(\d+)"', data).group(1))
	friends = re.findall("<name>(.*)</name>", data)
	user = friends[0]	#next user!

	print degree       # number of friends of "rj"
	print friends      # first 10 friends (because page=1 and limit=10).
	print user	
	sample_size = sample_size+1

