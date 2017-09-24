My_Pizzas = ["Mozarella", "Marinara","Margherita"]
Friend_Pizzas = My_Pizzas[:]
print(My_Pizzas)
print(Friend_Pizzas)

My_Pizzas.append('Pepperoni')
Friend_Pizzas.append('Meat Lover')

print("My favourite pizzas are:")
print(My_Pizzas)
for My_Pizza in My_Pizzas:
    print(My_Pizza)

print("My friends favourite pizzas are:")
print(Friend_Pizzas)
for Friend_Pizza in Friend_Pizzas:
    print(Friend_Pizza)

