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

