import sys

def primes_gen():
  primes = []
  i = 2
  while True:
    is_i_prime = True
    for p in primes:
      if i % p == 0:
        is_i_prime = False
        break
    if is_i_prime:
      primes.append(i)
      yield i
    i += 1

def find_nth_prime(n):
  primes = primes_gen()
  ith_prime = None
  for i in xrange(1, n+1):
    ith_prime = primes.next()
    print "Prime #{} is {}".format(i, ith_prime)
  return ith_prime

if __name__ == "__main__":
  print find_nth_prime(int(sys.argv[1]))
