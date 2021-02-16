store_items = {'Potato':20,'Tomato':10,'Egg':2,'Apple':100,'Chicken': 500,'Soap':10,'Onion':1.5,'Oil':1.2, 'Milk':30}

Cart = {}

print('Hello!')
print('Welcome to R Store. \nThankyou for choosing our store.\nPlease go ahead to buy something.')
print('Our store contains :\n')
for product, price in store_items.items():
    if ('Oil' in product) or ('Milk' in product):
        print(product,': $',price,'/liter.')

    elif ('Egg' in product) or ('Soap' in product):
        print(product,': $',price,'/piece.')
    else:
        print(product,': $',price,'/kg')
print()

while True:
    products=(input('What do you want? : '))
    if ('Potato' in products) or ('Onion' in products) or ('Chicken' in products) or ('Apple' in products) or ('Tomato' in products) :
        quantities = float(input('How much do you want in Kg : '))

    elif ('Oil' in products) or ('Milk' in products):
        quantities = float(input('How much do you want in liter : '))
    else:
        quantities = float(input('How much do you want in piece : '))
    
    Cart[products] = quantities

    
    user_said = input('Want more items ? (Yes/No) : ').lower()
    
    if ('yes' in user_said) and ('no' in user_said):
        user_said = input('Invalid answer.\nDo you want more items? (Yes/No): ').lower()
        if 'no' == user_said:
            break
        else:
            continue
    elif 'yes' in user_said:
        continue
    else:
        break
    
    

Total = 0
for product, quantity in Cart.items():
    Total += store_items[product] * quantity
    if ('Egg' in product) or ('Soap' in product):
        x=store_items[product]*quantity
        print(product,':$',store_items[product],'/piece *',quantity,'piece =  $',x)

    elif ('Oil' in product) or ('Milk' in product):
        y=x=store_items[product]*quantity
        print(product,':$',store_items[product],'/liter *',quantity,'liter =  $',y)
    else:
        z=x=store_items[product]*quantity
        print(product,':$',store_items[product],'/kg *',quantity,'kg =  $',z)


print('\nYour Total price $',int(Total))

while True:
    Total_money= int(input('Please pay the price:$'))
    if Total_money == int(Total):
        print('Thank you for shopping!\nVisit again! :)')
        break
    elif Total_money > Total:
        change = Total_money - int(Total)
        
        print('Thank you for shopping, here is the change $', change,'\nvisit again!')
        break
    else:
        c=int(Total)-Total_money
        print('Sorry, but you need to pay $',c,'more\nThank you for shopping\nvisit again!')
        break

    
