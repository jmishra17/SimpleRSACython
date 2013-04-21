%cython
'''
	Name - Abhishek Mishra
	Student id - 0934024
	Email - abhism@uw.edu
	File - SimpleRSA.py
	Instructor - William Stein
	Course - Math 480 Spring 2013
	Description: This program is a class model for generating a simple public-key encryption using
	the RSA model. 
'''
import math
from random import choice
from random import randint
import sys
import time
import fractions

cdef class SimpleRSA:
	cdef unsigned long limit, n, totient, e, d
	cdef int debug
	def __cinit__(self, unsigned long limit=sys.maxsize):
		self.debug =0
		self.limit = limit
		self.n = 0
		self.totient = 0
		self.e = 0
		self.d = 0
		
		
	'''	Main method for computing public-key and private-key	and storing
		 them as object class fields'''
	def compute(self):
		cdef unsigned long p = randint(self.limit,2*self.limit)
		cdef unsigned long q = 	randint(self.limit,2*self.limit)
		self.n = self.karatsuba(p,q,2)
		self.totient = self.karatsuba(p-1,q-1,2)
		self.e = randint(2,self.totient-1)
		while (fractions.gcd(self.e,self.totient) != 1):
			self.e = randint(2,self.totient-1)
		self.d = self.modulo_mult_inverse(self.e, self.totient)
		print("public key", (self.n,self.e))
		print("private key", (self.n,self.d))

	# Method that calculates extended greatest common divisor for two integers 
	# a and b.
	def extended_gcd(self,unsigned long b, unsigned long a):
		cdef unsigned long x = 0 
		cdef unsigned long lastx = 1
		cdef unsigned long y = 1
		cdef unsigned long lasty = 0
		cdef unsigned long quotient,remainder,m,n
		while a!=0:
			quotient = b//a
			remainder = b%a
			if self.debug==1:	
				print("quotient",quotient)
				print("remainder",remainder)
			
			m = x - lastx*quotient
			n = y - lasty*quotient
			if self.debug==1:
				print("m = x - lastx*quotient:",x,"-",lastx,"*",quotient,"=",m)
				print("n = y = lasty*quotient: ",y,"-",lasty,"*",quotient,"=",n)
			
			b = a
			a = remainder
			if self.debug==1:	
				print("b = a: b =",a)
				print("a = remainder: a =",remainder)
			
			x = lastx
			y = lasty
		
			if self.debug==1:
				print("x = lastx: x=",lastx)
				print("y = lasty: y=",lasty)
			
			lastx = m
			lasty = n
			if self.debug==1:	
				print("lastx = m: lastx = ",m)
				print("lasty = n: lasty = ",n)
				print("--------------------------------------")
			
		return	(b,x,y)
	
	
	'''Method for calculating modulo multiplicative inverse of integer e given by
		the equation 
			d*e mod(phi(n)) = 1  
		where d is the modulo multiplicative inverse, e is the parameter being considered,
		and phi(n) is the totient of n (totient if n=p*q = (p-1)*(q-1) = phi(n))
	''' 
	def modulo_mult_inverse(self,unsigned long e, unsigned long totient):
		cdef unsigned long b=-1
		cdef unsigned long x=-1
		cdef unsigned long y=-1
		b,x,y = self.extended_gcd(totient, e)
		if b == 1:
			return x%totient
		return None
		
	'''	
		Uses the Karatsuba multiplication algorithm for multiplying two numbers in 
		O(n^1.585) runtime. This is much faster compared to the traditional O(n^2)
		normal multiplication method.
	'''
	def karatsuba(self,unsigned long x,unsigned long y, int b):
		cdef int num_half_bitsX = len(str(x))/2
		cdef int num_half_bitsY = len(str(y))/2
		cdef int m =-1
		if num_half_bitsX < num_half_bitsY: 
			m = num_half_bitsX
		else:
			m = num_half_bitsY
		cdef unsigned long coeff = b**m	
		if x <1000 or y < 1000:
			return x*y
		cdef unsigned long x1 = x / coeff
		cdef unsigned long x0 = x % (x1 * coeff)
		cdef unsigned long y1 = y / coeff
		cdef unsigned long y0 = y % (y1 * coeff)
			
		cdef unsigned long p0 = self.karatsuba(x0,y0,b)
		cdef unsigned long p2 = self.karatsuba(x1,y1,b)
		cdef unsigned long q  = self.karatsuba((x0+x1),(y0+y1),b)
		cdef unsigned long p1 = q - p0 - p2
		cdef unsigned long sum_first = self.karatsuba(p2, coeff, b) + p1
		cdef unsigned long sum_final = self.karatsuba(sum_first, coeff, b) + p0	
		return sum_final		
		
		
def test(unsigned long n, unsigned long baseLimit, unsigned long incrmtFactor):
	cdef unsigned long lim = baseLimit
	cdef unsigned long start=-1
	cdef unsigned long diff=-1
	cdef SimpleRSA enc=None
	for i in range(1,n+1):
		lim = lim*incrmtFactor
		start=time.time()
		print("---------TEST"+str(i)+"---------")
		print("Limit = "+str(lim))
		print("-------")
		enc=SimpleRSA(lim)
		enc.compute()
		print("-------")
		diff = time.time() - start
		print("Time(seconds): "+str(diff))
		print("---------TEST"+str(i)+"---------")
		print("")
		print("")