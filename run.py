import jwt,sys, time

from base64 import b64decode as d
from base64 import b64encode as e
from jwt.utils import base64url_decode
from jwt.utils import base64url_encode
from jwt.algorithms import get_default_algorithms

wordlist = "rockyou.txt" # use the wordlist you want here
pl = open(wordlist, 'r') 
start = time.time()
counter = 1

token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoic2FpZiJ9.RCLja74dRw-ClVarLErLtTl0MaGkzUEabh353max73g'

algorithms = get_default_algorithms()
msg, r, signature_part = token.rpartition(b'.')
header = {u"typ":u"JWT", u"alg":u"HS256"}
algo = algorithms[header['alg']]
signature = base64url_decode(signature_part)

for i in pl:

	key = bytes(i.strip())
	if algo.verify(msg, key, signature) == True:
		print "+++++++++++++++++++++++++++++key found+++++++++++++++++++++++++++++\nAfter "+ str(counter) +" Tries \nKey is: '%s'"%str(i).strip()
		print "Average speed: %d per second"%(counter/(time.time()- start))
		exit(0)
	else:
		data = "Trying password number %d" %counter
		sys.stdout.write('%s\r' %data)
		sys.stdout.flush()
		counter += 1

print "Key not found :("
