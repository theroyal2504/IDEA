#p = 1
#for p in 10 :
 #   print(p)
#print()

#The range() function returns a sequence of numbers,
#starting from 0 by default, and increments by 1 (by default),
#and stops before a specified number.
for n in range(5,50,5):
    print(n)
print()

#In the range pass 2 paramitter range (star, stop)
#We are using the range function in which we are passing
#the starting and stopping points of the loop.
for m in range(2,11):
    print(m)
print()

#When the user call range() with three arguments,
#the user can choose not only where the series of
#numbers will start and stop
#If the user doesn’t provide a step, then range() will
#automatically behave as if the step is 1. In this example,
#we are printing even numbers between 0 and 10, so we choose
#our starting point from 0(start = 0) and stop the series at
#10(stop = 10). For printing an even number the difference
#between one number and the next must be 2 (step = 2) after
#providing a step we get the following output (0, 2, 4, 8).
#multiparamitter  range(start ,stop, step)
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