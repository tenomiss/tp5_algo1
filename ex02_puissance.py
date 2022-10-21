#!/usr/bin/python3

import time

def puissance_A(a,n):
  r = 1
  p = n
  while p>0:
    r = r*a
    p = p-1
  return r

def puissance_B(a,n):
  r = 1
  x = a
  p = n
  while p>0:
    if p%2==1:
      r = r*x
    p = p//2
    x = x*x
  return r

a = 54


for i in range(6):
  t0 = time.time()
  n = 10**i
  puissance_A(a,n)
  t1 = time.time()
  print(n)
  print(t1-t0)

print("__________________________________")
print("          fonction 2              ")
print("__________________________________")


for i in range(6):
  t0 = time.time()
  n = 10**i

  puissance_B(a,n)
  t1 = time.time()
  print(n)
  print(t1-t0)




