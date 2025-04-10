import math

def square(x):
  perimetr = x * 4
  ploshad = x * x
  diagonal = x * math.sqrt(2)
  return (perimetr, ploshad, diagonal)

print(square(5))