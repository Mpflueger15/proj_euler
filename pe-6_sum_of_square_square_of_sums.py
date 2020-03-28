def difference():
	sum_of_squares = sum([n**2 for n in range(1,101)])
	square_of_sums = ((100*(101))/2)**2
	return square_of_sums-sum_of_squares

print difference()