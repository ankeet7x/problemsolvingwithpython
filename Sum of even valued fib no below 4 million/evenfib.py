

def fib_calc():
	global sum
	sum = 0
	a = int(input("a = "))
	b = int(input("b = "))
	while b < 4000000:
		c = a + b
		a = b
		b = c
		if c % 2 == 0:
			sum = sum + c

def output_func():
	print(sum)



fib_calc()
output_func()
