list = [2,4,5,6,7,8,9,9,1,3,4,5,6,7]
choose = 0
while True:
    print("List  all element are excuted 'List' ", list)
    print(" 1.  Append an element")
    print(" 2.  Insert the element in the position")
    print(" 3.  Append a list to the given list ")
    print(" 4.  Modify an existing element ")
    print(" 5.  Delet in element in the position ")
    print(" 6.  Delet in element by its value ")
    print(" 7.  Sort the list in ascending order  ")
    print(" 8.  Sort the list in descending order ")
    print(" 9.  Display the list ")
    print(" 10. Exit")
    choose = int(input("Enter your choice performence (1-10) :"))
    if choose == 1:
        element = int(input("Enter the element to be append: " ))
        list.append(element)
        print("element append succefully\n")
        print(list)
        print("\n")
        continue
    elif choose == 2:
        element = int(input("Enter the element to be append: " ))
        position = int(input("enter the position to add element: "))
        list.insert(position,element)
        print("element append in the  given position  in succesfully\n")
    elif choose == 3:
        newList = int(input("Enter the element to be append: " ))
        list.extend(newList)
        print("new list add on existing list \n")
    elif choose == 4:
         i = int(input("enter the any of the position on the list :"))
         if i < len(list):
            newListElement = int(input("enter the new element  to modify possition of the list :"))
            list[i] = newListElement
            oldelement = list[i]
            print("the element ", oldelement,"has been mofield")
    elif choose == 5:


    elif choose == 6:


    elif choose == 7:
    

    elif choose == 8:
    

    elif choose == 9:


    elif choose == 10:
        break

print("exite with while loop")
