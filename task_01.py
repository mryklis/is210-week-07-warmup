def fibonacci(maxint):
	a, b = 0, 1
	fib_list = [a]
	while b < maxint:
		fib_list.append(b)
		a, b = b, a+b
	return fib_list
