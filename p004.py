def is_palindrome(n):
  s = str(n)
  return s == s[::-1]


def find_largest_palindrome_product_of_three_digit_numbers():
  # brute force; O(n^2) time, O(n^2) space
  prods = sorted([
      x * y
      for x in xrange(999, 100, -1)
      for y in xrange(x, 100, -1)],
    reverse=True)
  for prod in prods:
    if is_palindrome(prod):
      return prod

print find_largest_palindrome_product_of_three_digit_numbers()
