
def squareofsum():
	global sq_sum
	sq_sum = 0
	for n in range(101):
		sq_sum = sq_sum + n*n
	print(sq_sum)

def sumofsquare():
	global sum_sq
	sum = 0
	for n in range(101):
		sum = sum + n
	sum_sq = sum * sum
	print(sum_sq)


def diff_func():
	diff = sum_sq - sq_sum
	print(diff)

sumofsquare()
squareofsum()
diff_func()