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
xa, q = private
print "this is private key"+str(private)
print "this is public key"+str(public)
int_xa = int(xa)
ya = (a**int_xa)%q
sharedkey = str(ya)
paketserver = (public, sharedkey)
paketserver2 = pickle.dumps(paketserver)
counter = 0

s = socket.socket()
host = '127.0.0.1'
port = 12241
s.bind((host, port))
s.listen(5)
c = None

while True:
	counter = counter + 1
	if c is None:
		print 'menunggu koneksi dari server'
		c, addr = s.accept()
		print 'mendapatkan koneksi dari client dengan IP : ',addr
	else:
		if counter == 2:
			paketclient2 = c.recv(1024)
			paketclient = pickle.loads(paketclient2)
			print paketclient
			publicclient = paketclient[0]
			ybclient = paketclient[1]
			publickey, n = publicclient
			# print('ini yb-> ',yb)
			c.send(paketserver2)
			kab = (int(ybclient)**publickey)%n
			# print('ini kab-> ',kab)
			key = str(kab)

			count = 0

			if len(key) < 16:
				temp_key = len(key)
				while temp_key < 16:
					temp_key = temp_key + 1
					key = key + str(count)
					# print("cek isi-> ", key)
			print key

		pesan_belum = c.recv(1024)
		print pesan_belum
		cmd = ["python", "decrypt-des.py", "%s" %pesan_belum.strip(), "%s" %key]
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		decryptedmsg = proc.stdout.readlines()[2]
		print decryptedmsg
		
		q = raw_input("Tulis pesan: ")
		cmd = ["python", "des.py", "%s" %q.strip(), "%s" %key]
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		encryptedmsg = proc.stdout.readlines()[2]
		# print encryptedmsg
		c.send(encryptedmsg)