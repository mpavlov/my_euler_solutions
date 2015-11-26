divisible = lambda x: x % 5 == 0 or x % 3 == 0
print sum((x for x in xrange(1000) if divisible(x)))
