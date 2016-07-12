"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a not equal b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def factors(n):
    return reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))

def isAmicablePair(n):
    f1 = sum(factors(n))-n
    f2 = sum(factors(f1))-f1
    return [n,f1] if n == f2 and f1 != f2 else None

def main():
    cache = {}
    for n in range(1,10001):
        if n not in cache:
            pair = isAmicablePair(n)
            if pair:
                x,y = pair[0],pair[1]
                cache[x],cache[y] = x,y

    print "sum: ", sum(cache.values())
    print "pairs: ", cache.values()

    return 0

main()
