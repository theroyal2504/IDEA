meenu = {
    'fridrice' : 150,
    'manchuriyan' : 100,
    'dominoes' : 120,
    'sandwitch' : 110,
    'coldrink'  :  60,
    'hot coffi'  : 90,
    'tea' : 40,
}

for keys in meenu:
    print(keys)

order_amount = 0
order1 = input("Enter first order = ")
if order1 in meenu:
    order_amount += meenu[order1]
    print(order_amount)
    print(f'your order {order1} submitted')
    while True:
             permission = input("do your have add order (yas/not) = ")
             if permission == "yas":
                     Addorder = input("Add the dis  in order = ")
                     order_amount += meenu[Addorder]
                     print(order_amount)
             else:
                     print(f'thankyou sir/maim total amount is {order_amount}')
                     break
else:
         print(f'your itean  {order1} is not availeblyet')


