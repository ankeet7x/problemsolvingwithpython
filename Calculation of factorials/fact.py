
def input_func():
	global num
	num = int(input("Enter a number"))


def primefactor_checker():
	ch_num = num
	x = (ch_num//2) + 1
	for i in range(2, x):
		if ch_num % i == 0:
			# ch_num = ch_num // i
			print(i)



input_func()
primefactor_checker()