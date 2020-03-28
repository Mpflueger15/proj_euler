def primes(n):
	nums = [True]*(n+1)
	nums[0]=False
	nums[1]=False
	for i in range(2,n):
		j=0
		if nums[i]:
			while i*(i+j)<=n:
				nums[i*(i+j)]=False
				j+=1
	return sum([i for i in range(2,n) if nums[i]])

print(primes(2000000))