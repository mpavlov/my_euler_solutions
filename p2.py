seclast, last = 0, 1
total = 0
while True:
  curr = last + seclast
  if curr > 4000000:
    break
  if curr % 2 == 0:
    total += curr
  seclast, last = last, curr
print total
