import sys
from operator import mul
from p003 import naive_factorization

def common_factors_for(numbers):
  factors = {}
  for n in numbers:
    factors_for_n = naive_factorization(n)
    for factor in factors_for_n:
      factors[factor] = max(factors_for_n[factor], factors.get(factor, 0))
  return factors

if __name__ == "__main__":
  numbers = range(1, int(sys.argv[1]) + 1)
  factors = common_factors_for(numbers)
  print reduce(mul, [factor**power for factor, power in factors.items()], 1)
