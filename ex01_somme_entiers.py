#!/usr/bin/python3

import time

def somme_entiers_1(n):
  somme = 0
  for i in range(1,n+1):
    somme += i
  return somme

def somme_entiers_2(n):
  somme = n*(n+1)//2
  return somme




for i in range(7):
  temps0 = time.time()
  n = 10**i
  somme_entiers_1(n)
  temps1 = time.time()
  print(n)
  print(temps1 - temps0)

print("____________________________________")
print("        partie 2 (fonction2)")
print("____________________________________")
#2

for b in range(10):
  temps2 = time.time()
  n = 10**b
  somme_entiers_2(n)
  temps3 = time.time()
  print(n)
  print(temps3-temps2)




