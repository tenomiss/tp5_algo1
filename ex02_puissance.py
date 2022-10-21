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
