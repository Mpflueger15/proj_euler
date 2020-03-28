def multiply_list(prod):
	answer = 1
	for p in prod:
		answer *= p
	return answer

def divisible(n):
	for i in range(1,21):
		if n%i != 0:
			return False
	return True

def largest_multiple():
	#comp = [4,6,8,9,10,12,14,15,16,18,20]
	#primefact = [,,3,,,3,]
	primefact = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
	#prime = [2, 3, 5, 7, 11, 13, 17, 19]
	"""
	for n in range(9699690, 378224641, 4):
		print n
		for c in comp:
			if n%c != 0:
				break
	"""
	return multiply_list(primefact)

print largest_multiple(), divisible(largest_multiple())

