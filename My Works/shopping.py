foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        price = int(input(f'Enter the price of {food} : '))
        prices.append(price)
        foods.append(food)


print("----Your Cart----")
for food in foods:
    print(food, end=' ')
print()
for price in prices:
    total += price

print(f'total is : {total}')
