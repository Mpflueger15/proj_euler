def fibonacci():
	i = 0
	fib = [1,1]
	while i < 4000000:
	    i = fib[len(fib)-1]+fib[len(fib)-2]
	    fib.append(i)
	return fib

def sum_even():
	fib = fibonacci()
	return sum([f for f in fib if f % 2 == 0])

print sum_even()