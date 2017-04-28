import socket
import subprocess

q = 353
a = 3

xb = input('masukkan random key (xb) : ')
int_xb = int(xb)
yb = (a**int_xb)%q
sharedkey = str(yb)
print('ini yb-> ', yb)

counter = 0

s = socket.socket()
host = socket.gethostname()
port = 12234

s.connect((host, port))
print 'Terhubung dengan server dengan IP : ', host

while True:
	counter = counter + 1

	# print ("-> ", counter)
	if counter == 1:
		s.sendall(jebret)
		ya = s.recv(10)
		# print ('ini ya->', ya)
		kab = (int(ya)**int_xb)%q
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

