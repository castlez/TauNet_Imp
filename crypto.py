#TauNet Encryption Tools
#Copyright (c) 2015 Jonathan Castle

import os

def rc4(n, r, k):
	l = len(k)
	s = list(range(256))
	j = 0
	for t in range(r):
		for i in range(256):
			j = (j + s[i] + k[i%l]) % 256
			s[i],s[j] = s[j],s[i]
	keyStream = list(range(n))
	j = 0
	for i in range(n):
		p = (i+1)%256
		j = (j+s[p])%256
		s[p],s[j] = s[j],s[p]
		keyStream[i] = s[(s[p] + s[j])%256]
			
	return keyStream

def encrypt(m,r,k):
	n = len(m)
	iv = os.urandom(10)
	l = k + iv
	keyStream = rc4(n,r,l)
	cipher = list(range(n+10))
	for i in range(0,10):
		cipher[i] = iv[i]
	for i in range(n):
		cipher[i+10] = ord(m[i]) ^ keyStream[i] 
	return bytes(cipher)
	
def decrypt(m,r,k):
	n = len(m)
	iv = m[0:10]
	m = m[10:n]
	p = k + iv
	keyStream = rc4(n-10,r,p)
	toReturn = ""
	for i in range(0,n-10):
		toReturn += chr(m[i] ^ keyStream[i])
	return str(toReturn)
	
