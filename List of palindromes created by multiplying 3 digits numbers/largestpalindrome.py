
def input_function():
	global y
	for i in range(100, 999):
		for j in range(100, 999):
			y = i*j
			palindrome_checker()

def palindrome_checker():
	
	list = []
	n = y
	sum = 0
	while(n != 0):
		x = n % 10
		sum = sum * 10 + x
		n = n // 10
	if(sum == y):
		list.append(sum)
		list.sort()
		print(list)


# COULDN'T SORT THE LIST :(


input_function()
