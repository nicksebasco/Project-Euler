"""
Been playing around with cython so I decided to utilize it in my last PE solution.
problem: 
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
proccess:
    (1) knowing that all numbers > 28123 can be expressed as the sum of two abundant numbers,
    test all numbers from 0-28123 for abundance, save abundant numbers in a set.  
    (2) Every time a new abundant number is found, store the sum of it and every previously found abundant number
    in another set, sums.  
    (3) after you test for abundance, and add any new sums to the "sums" set, test if the number (value of current iteration in for loop)
    is in the sums set.  If it is not, add the number to the "deficient" set and add the value to the 'deficient_sum' value; else, do
    nothing.
    (4) cache['deficient_sum'] holds the answer to the problem.
"""

from p23 import factors, isAbundant

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

print "Answer: ",cache['deficient_sum']
