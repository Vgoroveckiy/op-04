def bank(a, years):
  for i in range(years):
    a = a * 1.1
  return a

print(bank(100, 2))


