"""
def remove_zeros(n):
	num_list=list(enumerate(str(n)))
	zero_tuple_list = [n[0] for n in num_list if n[1] == '0']
	index_list = []
	for i in zero_tuple_list:
		for j in range(i-12,i+13):
			index_list.append(j)
	remain_num_list = [n for n in num_list if n[0] not in index_list]
	return remain_num_list

def index_list(prod_list):
	index_lists = []
	index_list = []
	for t in prod_list:
		try:
			if t[0] != index_list[len(index_list)-1]+1:
				index_lists.append(index_list)
				index_list = [t[0]]
				continue
			else:
				index_list.append(t[0])
		except:
			index_list.append(t[0])
	return index_lists

def product(prod_list):
	indexes=index_list(prod_list)
	for i in indexes:
"""
def product(number):
	num = str(number)
	prod_list = []
	prod = 1
	for i in range(0,len(num)-12):
		for j in range(i,i+13):
			try:
				prod *= int(num[j])
			except:
				pass
		prod_list.append(prod)
		prod = 1
	return max(prod_list)



def main():    
	number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
	#prod_list = remove_zeros(number)
	print(product(number))

main()