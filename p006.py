import sys

def sum_of_squares_up_to(n):
  return sum(x**2 for x in xrange(n+1))

def square_of_sum_up_to(n):
  return sum(xrange(n+1))**2

if __name__ == "__main__":
  n = int(sys.argv[1])
  print square_of_sum_up_to(n) - sum_of_squares_up_to(n)
