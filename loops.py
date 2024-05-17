#p = 1
#for p in 10 :
 #   print(p)
#print()


for n in range(5,50,5):
    print(n)
print()


for m in range(2,11):
    print(m)
print()


for s in range(1,11):
    print(s*5,end=" ")
print()

print("----------------------")
for s in range(1,11):
    print(s,end=" ")
print()

print("hellnk")
#in chain function are use range
from itertools import chain
res = chain(range(5),range(5,20,2))
for i in res:
    print(i,end=" ")
print()


#while loop
#number increament
i = 1
while  i <= 10:
    print(i,end=" ")
    i = i+1
print()


#number dicreament
a= 10
while a>=1:
    print(a,end=" ")
    a=a-1
print()
