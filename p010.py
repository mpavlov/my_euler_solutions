import sys

def sum_of_primes_under(n):
  primes = [True] * n
  primes[0], primes[1] = [False, False]  # 0 and 1 are not prime by convention
  for i in xrange(len(primes)):
    is_prime = primes[i]
    if is_prime:
      primes[2*i::i] = [False] * len(primes[2*i::i])
  return sum(i for i, is_prime in enumerate(primes) if is_prime)

if __name__ == "__main__":
  print sum_of_primes_under(int(sys.argv[1]))
