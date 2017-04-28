#!/usr/bin/python

def run():
	q=353 # publicly known must be prime
	a=3 # publicly known

	xa=97 # only client1 knows this 
	xb=233 # only client2 knows this

	client1Sends = (a**xa)%q
	client2Computes = (client1Sends**xb)%q
	client2Sends = (a**xb)%q
	client1Computes = (client2Sends**xa)%q


	print "client1 sends    ", client1Sends 
	print "client2 computes   ", client2Computes 
	print "client2 sends      ", client2Sends 
	print "client1 computes ", client1Computes

	print "In theory both should have ", (a**(xa*xb))%q

	return client1Sends, client2Computes, client2Sends, client1Computes

if __name__ == '__main__':
    run()