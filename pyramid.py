print ("-------1-------")
z = 6
for a in range(z):
    for j in range(z-a-1):
        print(" ", end="")
    for j in range(a+1):
          print(j+1,end=" ")
    print("\n")
print("end")
print("-----------------------------\n")
print ("-------2-------")
for a in range(6):
      for j in range(a+1):
          print("*",end=" ")
      print("\n")
print("end")
print("-----------------------------\n")
print ("-------3-------")
ascii_value = 65
for a in range(6):
      for j in range(a+1):
          alphabet = chr(ascii_value)
          print(alphabet,end=" ")
      ascii_value += 1
      print("\n")
print ("complite")
print("-----------------------------\n")

print ("-------4-------")
print( )

b = 1
while b<=6:
    i = 1
    while i<=b:
        print("*",end=" ")
        i += 1
    #print("*",end="")
    print("\n")
    b = b+1
print(" end")
print("-----------------------------\n")
print ("-------5-------")
print( )
for a in range(5,0,-1):
      for j in range(1,a+1):
          print("*",end=" ")
      print("\n")
      a = a + 1
print("end")
print()

print("-----------------------------\n")
print ("-------6-------")
b = 1
while b<=5:
    i = 5
    while i>=b:
        print("*", end=" ")
        i -= 1
    print("\n")
    b = b+1
print("end")
print("-----------------------------\n")
print ("-------7-------")
print()
k = 1
i = 1
while i <= 6:
    j = 1
    while j <= i:
        print(" ",format(k),end="")
        j += 1
        k += 1
    print("\n")
    i += 1
print("end")
print("-----------------------------\n")
print ("-------9-------")
k = 1
for i in range(1,7):
    for j in range(1,i+1):
        print(" ", format(k), end="")
        j += 1
        k += 1
    print()
    i += 1
print("-----------------------------\n")
print ("-------10-------")
for a in range(5,0,-1):
      for j in range(a):
          print("*",end=" ")
      print("\n")
print("end")
print("-----------------------------\n")
print ("-------11-------")
for z in range(5,0,-1):
    for j in range(1,z+1):
        print(j,end=" ")
    print("\n")
print("-----------------------------\n")

print ("-------12-------")
z= int(input("plss inter row for pyramid  "))
for i in range(0,z):
    for j in range(0,z-i-1):
        print(" ", end="")
    for j in range(0,i+1):
        print("* ", end="")
    print()





'''for i in range(1, z):
    for a in range(1, z-i):
        print("  ", end="")
    for j in range(i, 2*i):
        print("* ", end="")
    for j in range(1, i):
          print("* ",end="")
    print()

print("------------revers-----------------")
#z = int(input("plss inter row for pyramid  "))
for i in range(z-1,0,-1):
        for a in range(i,z-1):
             print("  ", end="")
        for j in range(i, 2*i):
            print("* ", end="")
        for j in range(1, i):
            print("* ", end="")
        print( )
print()'''
