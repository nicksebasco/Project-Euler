# calculate sum of digits in 100!
# solution is trivial in python

def fact(n):
	return n*fact(n-1) if n>1 else 1

def sum_digits(n):
	return sum([int(i) for i in list(str(n))])
	
def main():
	f100 = fact(100)
	sd = sum_digits(f100)
	print sd
main()

"""
# alternatively
fact = lambda n: n*fact(n-1) if n>1 else 1
sum_digits = lambda n: sum([int(i) for i in list(str(n))])
print sum_digits(fact(100))
"""
