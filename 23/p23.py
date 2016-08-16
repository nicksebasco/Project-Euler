from p23 import factors, abundant_numbers, isAbundant

limit = 28123
cache = {
    'abundant':      set(),
    'sums':          set(),
    'deficient':     set(),
    'deficient_sum': 0
    }

for i in range(limit):
    if isAbundant(i):
        cache['abundant'].add(i)
        for j in cache['abundant']:
            cache['sums'].add(i+j)
    if i not in cache['sums']:
        cache['deficient'].add(i)
        cache['deficient_sum'] = cache['deficient_sum'] + i

print "deficient sum: ",cache['deficient_sum']
