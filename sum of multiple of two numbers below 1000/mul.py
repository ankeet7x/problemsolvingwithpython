def input_function():
	global a, b
	a = int(input("Enter a"))
	b = int(input("Enter b"))


def mul_extraction():
	global sum
	sum = 0
	for i in range(1000):
		if i%a == 0 or i%b ==0:
			sum = sum + i

def output_function():
	print(sum)


input_function()
mul_extraction()
output_function()