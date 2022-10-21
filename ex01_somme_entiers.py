print("test")
#import time


def somme_entiers_1(n):
  somme = 0
  for i in range(1,n+1):
    somme += i
  return somme




def somme_entiers_2(n):
  somme = n*(n+1)//2
  return somme






temps0 = time.time()
  
for i in range(7):
    
    
  n=10^i
  somme_entiers_1(n)
  print(n)
    
    
temps1 = time.time()
    
print(temps1 - temps0)
  