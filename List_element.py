list1 = []
n = int(input("Enter the number of elements: "))

# Append elements to the list
for i in range(n):
    list = input(f"Enter element {i+1}: ")
    list1.append(list)

#list = [2,4,5,6,7,8,9,9,1,3,4,5,6,7]
choose = 0
while True:
    print("\n\nList  all element are excuted 'List' ", list1)
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
        list1.append(element)
        print("element append succefully\n")
        print(list)
        print("\n")
        continue
    
    elif choose == 2:
        element = int(input("Enter the element to be append: " ))
        position = int(input("enter the position to add element: "))
        list1.insert(position,element)
        print("element append in the  given position  in succesfully\n")
    
    elif choose == 3:
        newList = input("Enter the list to be append: " )
        list1.extend(newList)
        print("new list add on existing list \n")
    
    elif choose == 4:
        i = int(input("enter the any of the position on the list :"))
        if i < len(list):
            newListElement = int(input("enter the new element  to modify possition of the list :"))
            list1[i] = newListElement
            oldelement = list1[i]
            print("the element ", oldelement,"has been mofield")
    
    elif choose == 5:
        possition = int(input("enter the list of possition :"))
        if possition < len(list):
             new_list = list1.pop(possition)
             list_delet = list1[new_list]
             print("the element has" ,list_delet,"deleted succesfully")
             print("new list is := ", list1)
        else :
            print("given element position is gratter than to length of\n\n")
    
    elif choose == 6:
        element_value = int(input("enter the inlcuding element value := "))
        if element_value in list:
            list1.remove(element_value)
            print("the given valur",element_value, " succesfully remove ")
            print("new list is := ", list1)
        else:
            print("enter the element value",element_value,"not in list ")
    
    elif choose == 7:
        print(list1.sort())
        print("the list has been sorted succesfully Accending order ")
    
    elif choose == 8:
        list1.sort(reversed == True)
        print("the list has been sorted succesfully desending order ")
    
    elif choose == 9:
         print("the list is : =",list1)
    
    elif choose == 10:
         break

print("exite with while loop")
