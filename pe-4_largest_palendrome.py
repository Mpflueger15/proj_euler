def check(prod_str):
	for i in range(0,len(prod_str)//2):
		if prod_str[i]!=prod_str[len(prod_str)-1-i]:
			return False
	return True

def largest_palindrome():
	for j in range(999, 100, -1):
			prod = j*j
			if check(str(prod)):
				return prod
			prod = j*(j-1)
			if check(str(prod)):
				return prod
			prod = j*(j-2)
			if check(str(prod)):
				return prod
					
print largest_palindrome()

