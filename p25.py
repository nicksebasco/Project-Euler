
fib = [1,1]
n0,n1 = 1,1
index = 2

while True:
	n = fib[index-1] + fib[index-2]
	fib.append(n)
	index = index + 1
	if index > 10000:
		break

for i in range(len(fib)):
	if len(str(fib[i])) == 1000:
		print i+1,": ", len(str(fib[i]))
		print fib[i]
		break
