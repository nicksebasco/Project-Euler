# calculate sum of digits in 100!
# solution is trivial in python

def fact(n):
	total = 1
	while n > 0:
		total = total * n
		n = n - 1
	return total

def sum_digits(n):
	return sum([int(i) for i in list(str(n))])

def main():
	f100 = fact(100)
	sd = sum_digits(f100)
	print sd

main()
