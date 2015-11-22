import sys

def naive_factorization(n):
  pf = {}

  for i in xrange(2, n/2+1):
    if n == 1:
      break
    while n % i == 0:
      pf[i] = 1 if i not in pf else pf[i] + 1
      n /= i

  if n != 1:
    pf[n] = 1

  return pf

def print_factorization(pf):
  print " + ".join((
    "{}^{}".format(i, pf[i])
    for i in sorted(pf.keys(), reverse=True)))

if __name__ == "__main__":
  pf = naive_factorization(int(sys.argv[1]))
  print_factorization(pf)
