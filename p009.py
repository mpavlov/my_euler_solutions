import sys

def is_pythagorean_triplet(a, b, c):
  return a**2 + b**2 == c**2

def find_pythagorean_triplet_summing_to(n, starting_a=1):
  a = starting_a
  while True:
    b = a + 1
    while True:
      c = b + 1
      while True:
        the_sum = a + b + c
        if the_sum > n:
          break
        elif the_sum == n and is_pythagorean_triplet(a, b, c):
          return a, b, c
        else:
          c += 1
      if the_sum > n and c == b + 1:
        break
      else:
        b += 1
    if the_sum > n and b == a + 1:
      break
    else:
      a += 1
  return None

if __name__ == "__main__":
  n = sys.argv[1]
  triplet = find_pythagorean_triplet_summing_to(int(n))
  if triplet:
    print triplet
  else:
    print "No triplet exists that sums to %s" % n
