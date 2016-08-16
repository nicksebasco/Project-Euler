from libcpp.vector cimport vector
from libcpp.map cimport map
from libc.math cimport sqrt, floor

def factors(int n):
  cdef int i
  cdef vector[int] v
  for i in range(1,<int>sqrt(n)+1 ):
    if n % i == 0:
      v.push_back(i)
      if n/i != i and i != 1:
        v.push_back(n/i)
  return v

def vector_sum(vector[int] v):
  cdef int i, t = 0
  for i in v:
      t = t + i
  return t

def isAbundant(n):
  cdef vector[int] f = factors(n)
  return True if vector_sum(f) > n else False

def abundant_numbers(int min, int max):
  cdef vector[int] values = range(min,max+1), abundant, factor_list
  cdef int i, sum
  for i in values:
    factor_list = factors(i)
    sum = vector_sum(factor_list)
    # print [i,factor_list,sum],"\n"
    # test for abundance
    if sum > i:
      abundant.push_back(i)
  return abundant

"""
# iterate through abundant vector, if length > 1, add i to each j in abundant if j != i and append to abundant sums vector
# cdef map[int, int] abundant_sums
for j in abundant:
  if i != j:
    asum = i + j
    abundant_sums[asum] = asum
"""
