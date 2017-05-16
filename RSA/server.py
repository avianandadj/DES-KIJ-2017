import socket
import random
import string
import subprocess

q =353
a = 3

xa = input('Masukkan random key (xa): ')
int_xa = int(xa)
ya = (a**int_xa)%q
sharedkey = str(ya)

counter = 0

s = socket.socket()
host = socket.gethostname()
port = 12234
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
			yb = c.recv(10)
			# print('ini yb-> ',yb)
			c.send(sharedkey)
			kab = (int(yb)**int_xa)%q
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