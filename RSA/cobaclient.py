import socket
import subprocess
from rsa import *
import pickle
import random

a = 3

prime1 = random.randrange(11,20)
while is_prime(prime1) == False:
	prime1 = random.randrange(11,20)
print "ini prime1: "+str(prime1)
prime2 = random.randrange(21,30)
while is_prime(prime2) == False:
	prime2 = random.randrange(21,30)
print "ini prime2: "+str(prime2)
public, private = generate_keypair(prime1, prime2)
xb, q = private
print "this is private key"+str(private)
print "this is public key"+str(public)
int_xb = int(xb)
yb = (a**int_xb)%q
sharedkey = str(yb)
print('ini yb-> ', yb)
paketclient = (public, sharedkey)
paketclient2 = pickle.dumps(paketclient)

counter = 0

s = socket.socket()
host = "127.0.0.1"
port = 12241

s.connect((host, port))
print 'Terhubung dengan server dengan IP : ', host

while True:
	counter = counter + 1

	# print ("-> ", counter)
	if counter == 1:
		s.sendall(paketclient2)
		paketserver2 = s.recv(1024)
		paketserver = pickle.loads(paketserver2)
		print paketserver
		publicserver = paketserver[0]
		yaserver = paketserver[1]
		publickey, n = publicserver
		# print ('ini ya->', ya)
		kab = (int(yaserver)**publickey)%n
		# print ('ini kab->', kab)
		key = str(kab)

		count = 0

		if len(key) < 16:
			temp_key = len(key)
			while temp_key < 16:
				temp_key = temp_key + 1
				key = key + str(count)
		print key

	z = raw_input("Tulis pesan: ")
	cmd = ["python", "des.py", "%s" %z, "%s" %key]
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	encryptedmsg = proc.stdout.readlines()[2]
	# print encryptedmsg
	s.send(encryptedmsg)
	print 'Menunggu response'

	x = s.recv(1024)
	print  x

	cmd = ["python", "decrypt-des.py", "%s" %x.strip(), "%s" %key]
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	decryptedmsg = proc.stdout.readlines()[2]
	print decryptedmsg

