def prime(n):
	if n == 1:
		return 2
	primes = [2]
	check_number = 3 
	while n-1 > 0:
		for p in primes:
			if check_number % p == 0:
				break
			if p == primes[len(primes)-1]:
				primes.append(check_number)
				n -= 1
		check_number += 1
	return primes.pop()

while input != 0:
	input = int(raw_input("which prime do you want to know? (press 0 to quit)"))
	print prime(input)
