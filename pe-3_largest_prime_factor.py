def next_prime(p):
	prime = False
	while prime == False:
		p += 1
		prime = True
		for d in range (2,p):
			if p%d == 0:
				prime = False
	return p

def prime_factor(n):
	p = 2
	factor = 0
	factor_list = []
	while factor < n:
		factor = 0
		if n%p == 0:
			n = n/p
			factor = max(p, factor)
		p = next_prime(p)
		factor_list.append(factor)
	return factor_list

print prime_factor(600851475143),product(prime_factor(600851475143))

