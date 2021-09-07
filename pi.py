import random

total = 0
inside = 0

n = 5000000

while total <= n:
  x = random.uniform(1, -1)
  y = random.uniform(1, -1)

  if (x*x + y*y)**(0.5) <= 1:
    inside = inside + 1

pi = (4*inside)/n
print(pi)
