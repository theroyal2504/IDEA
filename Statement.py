num1 = int(input("Enter number fist :-"));
num2 = int(input("Enter number second :-"));
opr =  input("Enter the  operation (+,-,/,*) :-")
if opr=="+":
    print("value are sum",num2+num1)
elif opr=="-":
    print("value are minus" ,num1-num2)
elif opr=="/":
    print("value is divide ",num1/num2)
elif opr=="*":
    print("value are multiple",num2*num1)
else:
    print("Not valied operation")

print()
#nasted loop
if num1 > num2:
    print("num1 is bigest")
else:
    if num1< num2:
        print("num2 is bigest")
    else:
        print("both are equle")
