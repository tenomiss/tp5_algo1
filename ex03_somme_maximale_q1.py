#!/usr/bin/python3
import random

def tableau_aleatoire(n):
  tab = [0]*n
  for i in range(n):
    tab[i] = random.randint(0,n)
  return tab

def somme_maximale(tab):
  n = len(tab)
  maximum = tab[0]+tab[1]
  for i in range(n):
    for j in range(i+1,n):
      if tab[i]+tab[j]>maximum:
        maximum = tab[i]+tab[j]
  return maximum

def test_somme_maximale():
  print('Test de la fonction somme_maximale')
  assert somme_maximale([3,7])==10
  assert somme_maximale([8,2,4])==12
  assert somme_maximale([8,13,2,13,7,1])==26
  assert somme_maximale([9,6,12,11,9,3,17,1,19,0])==36
  assert somme_maximale([-9,-9,14,-18,5,-8,-9,11,10,-3])==25
  print('  OK')

test_somme_maximale()

