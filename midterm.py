n = raw_input("How many equations do you want?\n")

m = []
a = []
b = []
for i in range(0,int(n)):
	print "Equation", i+1
	a.append(raw_input("Enter the value of a\n"))
	b.append(raw_input("Enter the value of b\n"))
	m.append(raw_input("Enter the value of m\n"))

def euclidgcd(a, m):
	a = a % m
	if a == 0:
		return (m, 0, 1)
	else:
		d, y, x = euclidgcd(m % a, a)
		return (d, x - (m // a) * y, y)



def multiplicativeinverse(a, m):
	a = a % m
	d, x, y = euclidgcd(a, m)
	if d != 1:
		return 0;
	else:
		return x % m

print multiplicativeinverse(1, 1)
print multiplicativeinverse(6, 6)
print multiplicativeinverse(2, 6)

#def primefactorization(n):
#	output = []
#	i = 2
#	k = 1
#	while n != 1:
#		k = 1;
#		if n % i == 0:
#			while n % i == 0:
#				n = n/i
#				k = k * i
#			i = 2
#		i = i + 1
#		if k != 1:
#			output.append(k)
#	return output

#Gives a list of all primes in the factorization of n
def allprimesin(n):
	output = []
	i = 2
	k = 1
	while n != 1:
		if n % i == 0:
			output.append(i)
			while n % i == 0:
				n = n/i
			i = 2
		i = i + 1
	return output

#highest power of p that divides n
def vp(p, n):
	output = 0;
	while n % p == 0:
		n = n/p
		output = output + 1
	return output

def power(a, b):
	output = 1;
	for i in range(0,b):
		output = output*a;
	return output


#print allprimesin(12)
#print vp(2, 100)
#print power(2, 5)

#outputs the max of a and b
def maximumof(a, b):
	if a > b:
		return a
	else:
		return b

#print maximumof(100, 120)

#print a
#print b
#print m

print "Here are your equations:"
for i in range(0, int(n)):
	print a[i],"x =",b[i]," ( mod",m[i],")"


for i,j in enumerate(m):
	if int(m[i]) == 0:
		print "Modulo cannot be zero"
		quit()
	if int(a[i]) == 0 and int(b[i]) % int(m[i]) != 0:
		print "Equation", i+1, "is unsolvable"
		quit()

ainverses = []

for i,j in enumerate(a):
	ainv = multiplicativeinverse(int(j), int(m[i]))
	if ainv == 0:
		GCD,irrel, irrel2 = euclidgcd(int(j), int(m[i]))
		print "GCD is", GCD
		#print GCD
		if (int(b[i]) % int(m[i])) % GCD == 0:
			a[i] = int(a[i])/GCD
			b[i] = int(b[i])/GCD
			m[i] = int(m[i])/GCD
			print "a", a[i], "m", m[i]
			ainv = multiplicativeinverse(int(a[i]), int(m[i]))
			#if ainv == 0:
		#		print "case 1"
	#			print "Equation", i+1, "is unsolvable"
#				quit()
		else:
			print "case 2"
			print "Equation", i+1, "is unsolvable"
			quit()
	ainverses.append(ainv)


#foundaninverse = 0;
#for i,j in enumerate(m):
#	foundaninverse = 0;
#	for k in range(0, int(j)):
#		if k * int(a[i]) % int(j) == 1:
#			ainverses.append(k)
#			foundaninverse = 1
#	if foundaninverse == 0:
#		print "Equation", i, "is unsolvable"
#		quit()
#print ainverses
newb = []
for i,j in enumerate(b):
	newb.append(int(j) * ainverses[i] % int(m[i]))


for i in range(0,int(n)):
	for j in range(0,int(n)):
		GCD, irrel, irrel2 = euclidgcd(int(m[i]), int(m[j]))
		if ((int(newb[i]) - int(newb[j])) % GCD != 0):
			print "Equations", i+1, "and", j+1, "are not compatible"
			quit()


def solver(b, m):
	print "b is", b
	print "m is", m
	#print len(m)
	#print "there"
	if len(m) == 1:
		if int(m[0]) == 1:
			print "Solution is all integers"
			quit()
		else:
			print "Solution"
			print "x =", int(b[0]) % int(m[0]), "( mod", int(m[0]), ")"
			quit()


	if int(m[0]) == 1:
		m = m[1:]
		b = b[1:]
		solver(b, m)
	#productofm = 1
	#for i in m:
#		productofm = productofm * int(i)

	#newm = []
	#for i in m:
	#	newm.append(productofm/int(i))
	#y = []
	#for i,j in enumerate(m):
	#	for k in range(0,int(j)):
	#		if k*int(newm[i]) % int(j) == 1:
	#			y.append(k)
	GCD, irrel, irrel2 = euclidgcd(int(m[0]), int(m[1]))
	if GCD == 1:
		mcut = m[0:2]
		bcut = b[0:2]

		newm = []
		newm.append(m[1])
		newm.append(m[0])
		y = []
	#	for i,j in enumerate(mcut):
	#		for k in range(0, int(j)):
	#			if k * int(newm[i]) % int(j) == 1:
	#				y.append(k)
		for i,j in enumerate(mcut):
			yval = multiplicativeinverse(int(newm[i]), int(j))
			y.append(yval)

		output = 0;
		for i in range(0, 2):
			output = output + int(b[i]) * int(y[i]) * int(newm[i])

		m[1] = int(m[1])*int(m[0]);
		b[1] = output % int(m[1])

		m = m[1:]
		b = b[1:]

		solver(b, m)
	else:
		#m.append(GCD)
		#b.append(b[0])
		#m.append(int(m[0])/GCD)
		#b.append(b[0])
		#m.append(int(m[1])/GCD)
		#b.append(b[1])
		#b = b[2:]
		#m = m[2:]
		#solver(b,m)
		GCDprimes = allprimesin(int(m[0]) * int(m[1]))
		#print "Gcdprimes is", GCDprimes
		#m0factorization = primefactorization(int(m[0]))
		#m1factorization = primefactorization(int(m[1]))


		for i in GCDprimes:
			m0power = vp(i, int(m[0]))
			m1power = vp(i, int(m[1]))
			if m0power > m1power:
				m.append(power(i, m0power))
				b.append(int(b[0]))
			else:
				m.append(power(i, m1power))
				b.append(int(b[1]))

		m = m[2:]
		b = b[2:]
		solver(b, m)		




	#print a
	#print b
	#print m
	#print newm
	#print y


	#output = 0;

	#for i in range(0,int(n)):
	#	output = output + int(b[i])*int(y[i])*int(newm[i])


	#print "Solution:"
	#print "x =", output % productofm, "( mod", productofm, ")"

solver(newb, m)








