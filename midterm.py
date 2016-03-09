#euclidean algorithm to calculate GCD of a and m
def euclidgcd(a, m):
	a = a % m
	if a == 0:
		return (m, 0, 1)
	else:
		d, y, x = euclidgcd(m % a, a)
		return (d, x - (m // a) * y, y)


#calculates multiplicative inverse of a modulo m
def multiplicativeinverse(a, m):
	a = a % m
	d, x, y = euclidgcd(a, m)
	if d != 1:
		return 0;
	else:
		return x % m

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


#outputs a^b
def power(a, b):
	output = 1;
	for i in range(0,b):
		output = output*a;
	return output

def solver(b, m):
	if len(m) == 1:
		#if there is only one equation left and the modulo is 1, then the solution is all integers
		if int(m[0]) == 1:
			print "Solution is all integers"
			quit()
		else:
			#otherwise just print the only solution
			print "Solution"
			print "x =", int(b[0]) % int(m[0]), "( mod", int(m[0]), ")"
			quit()

	#if the modulo of the first equation is one, then just remove that equation and solve the remaining equations
	if int(m[0]) == 1:
		m = m[1:]
		b = b[1:]
		solver(b, m)

	GCD, irrel, irrel2 = euclidgcd(int(m[0]), int(m[1]))
	#if the GCD is 1
	if GCD == 1:
		mcut = m[0:2]
		bcut = b[0:2]

		newm = []
		newm.append(m[1])
		newm.append(m[0])
		y = []

		for i,j in enumerate(mcut):
			yval = multiplicativeinverse(int(newm[i]), int(j))
			y.append(yval)

		output = 0;
		for i in range(0, 2):
			output = output + int(b[i]) * int(y[i]) * int(newm[i])

		#assign the results to index 1 of m and b, and cut off the index 0 elements, then solve from here.
		m[1] = int(m[1])*int(m[0]);
		b[1] = output % int(m[1])

		m = m[1:]
		b = b[1:]

		solver(b, m)
	else:
		GCDprimes = allprimesin(int(m[0]) * int(m[1]))

		#for each prime in either m[0] or m[1], only the highest power matters, so choose whichever has the highest power of that prime and then append it to the end
		for i in GCDprimes:
			m0power = vp(i, int(m[0]))
			m1power = vp(i, int(m[1]))
			if m0power > m1power:
				m.append(power(i, m0power))
				b.append(int(b[0]))
			else:
				m.append(power(i, m1power))
				b.append(int(b[1]))

		#cut off the first two elements and then solve from there
		m = m[2:]
		b = b[2:]
		solver(b, m)

#inputs the number of equations
n = raw_input("How many equations do you want?\n")
if int(n) <= 0:
	print "The number of equations has to be positive"
	quit()

m = []
a = []
b = []

#inputs the values of ai, bi, and mi
for i in range(0,int(n)):
	print "Equation", i+1
	a.append(raw_input("Enter the value of a\n"))
	b.append(raw_input("Enter the value of b\n"))
	m.append(raw_input("Enter the value of m\n"))


#prints all equations
print "Here are your equations:"
for i in range(0, int(n)):
	print a[i],"x =",b[i]," ( mod",m[i],")"


#first, cleans the numbers
for i,j in enumerate(m):
	#makes negative modulo's positive
	if int(m[i]) < 0:
		m[i] = -1 * int(m[i])
	#quits if one of the modulo's is zero
	if int(m[i]) == 0:
		print "Modulo cannot be zero"
		quit()
	#quits if a modulo m is 0 and b modulo m is not zero
	if int(a[i]) % int(m[i]) == 0 and int(b[i]) % int(m[i]) != 0:
		print "Equation", i+1, "is unsolvable"
		quit()
	#converts a and b to their canonical residue modulo m, between 0 and m-1
	b[i] = int(b[i]) % int(m[i])
	a[i] = int(a[i]) % int(m[i])

ainverses = []

#creates the list of inverses of a modulo m
for i,j in enumerate(a):
	ainv = multiplicativeinverse(int(j), int(m[i]))
	#ainv = 0 if the multiplicative inverse does not exist
	if ainv == 0:
		GCD,irrel, irrel2 = euclidgcd(int(j), int(m[i]))
		#divide everything by GCD. The case where m = 1 will be taken care of later.
		if (int(b[i]) % int(m[i])) % GCD == 0:
			a[i] = int(a[i])/GCD
			b[i] = int(b[i])/GCD
			m[i] = int(m[i])/GCD
			ainv = multiplicativeinverse(int(a[i]), int(m[i]))
		else:
			print "Equation", i+1, "is unsolvable"
			quit()
	ainverses.append(ainv)

newb = []
#multiply by the inverses so we have a system where all the x's have coefficient one.
for i,j in enumerate(b):
	newb.append(int(j) * ainverses[i] % int(m[i]))


#checks if any two equations are incompatible, quits if any two are.
for i in range(0,int(n)):
	for j in range(0,int(n)):
		GCD, irrel, irrel2 = euclidgcd(int(m[i]), int(m[j]))
		if ((int(newb[i]) - int(newb[j])) % GCD != 0):
			print "Equations", i+1, "and", j+1, "are not compatible"
			quit()

#calls the solver function
solver(newb, m)








