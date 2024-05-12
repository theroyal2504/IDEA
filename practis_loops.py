z = int(input("plss inter row for pyramid "))

print("-----------------------------")
for i in range(1, z):
    for a in range(1, z-i):
        print("  ", end="")
    for j in range(i, 2*i):
        print("* ", end="")
    for j in range(1, i):
          print("* ",end="")
    print()
print("------------revers-----------------")
#j = int(input("plss inter row for pyramid  "))
for i in range(z-1,0,-1):
        for a in range(i,z-1):
             print("  ", end="")
        for j in range(i, 2*i):
            print("* ", end="")
        for j in range(1, i):
            print("* ", end="")
        print( )
print()
print("--------------2---------------")
for i in range(1,z):
    for x in range(1,i+1):
        print("*",end=" ")
    print()
print("---------------3--------------")
for i in range(1,z,):
    for x in range(1,z-i):
        print(" ",end=" ")
    for a in range(1,i+1):
        print("*",end=" ")
    print()
print("----------------4-------------")
for f in range(z,1,-1):
    for x in range(f,1,-1):
        print("*",end=" ")
    print()
print("-----------------5------------")
for i in range(z,0,-1):
    for f in range(0,z-i):
        print(" ", end=" ")
    for m in range(1,i+1):
        print("*", end=" ")
    print()

print("-----------------NUMBER-----------")
a = 65
for i in range(1,z):
    for x in range(1,i+1):
        b = chr(a)
        print(b,end=" ")
        a += 1
    print()