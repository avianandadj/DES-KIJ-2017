import random


#fungsi gcd (greatest common divisor) 
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a



#cek apakah bilangan yang dimasukkan bilangan prima
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

#fungsi mendapatkan key
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #nilai n didapat dari perkalian p dan q
    n = p * q

    #mencari nilai phi
    phi = (p-1) * (q-1)
    print phi
    #tentukan nilai e untuk public key
    e = 7
    print e

    #mengecek apakah nilai gcd e dan phi adalah 1 
    g = gcd(e, phi)
    while g != 1:
        e = 7
        g = gcd(e, phi)

    #mengecek nilai private key (d) dengan algoritma extended euclidean
    # d = extended_euclidean(e, phi)
    d = random.randrange(1,1000)
    while (d * e) % phi != 1:
        d = random.randrange(1,1000)
  
    #didapatkan nilai private key (d,n) dan public key (e,n)
    return ((e, n), (d, n))

