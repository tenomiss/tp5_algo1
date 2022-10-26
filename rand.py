


import random,time
from tkinter import Y

list = [0, 2 , 10, 30, 1, 230]
x = 0
i = 0
y = 0
m = int(input("zizi"))


t0 = time.time()
while i < m :
    if x in list :
        print("true")
        i+=1
        
    else :
        list.append(y)
        i+=1
    y = random.randint(0, 1000)
    x = random.randint(0, 1000)
        
t1 = time.time()

print(t1-t0)

