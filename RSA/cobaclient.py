import socket
import subprocess
from rsa import *
import pickle

a = 3

prime1 = 11
prime2 = 17
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
host = socket.gethostname()
port = 12240

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

