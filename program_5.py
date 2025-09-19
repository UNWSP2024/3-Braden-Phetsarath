# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
#Braden Phetsarath
#9/19
#Hot Dog Order
def hot_dog_order():
    menu = ("Hot dogs \nClassic ($3.50), Chili Dog ($4.50) "
                "\nToppings \nCheese ($0.50), Peppers ($0.75), or Grilled onions ($1.00) ")
    print(menu)
    order = (str(input("Enter your Hot Dog: ")))
    if order == "Classic Dog": c = 3.50
    if order == "Chili Dog": c = 4.50
    #c = cost of the main order
    print ("Type one for yes")
    x = int(input("Do you want Cheese?"))
    if x == 1: x= 0.5
    else: x = 0
    y = int(input("Do you want Peppers?"))
    if y == 1:y = 0.75
    else: y = 0
    z = int(input("Do you want Onions?"))
    if z == 1:z=1
    else: z = 0
    t = c + x + y + z
    #t is the cost of the order without tax
    totalT = t + (.07*t)

    #totalT means total after tax
    print (order, "\nToppings")
    if x >0 : print('Cheese')
    if y >0 : print('Peppers')
    if z >0 : print('Onions')
    else: print('None')
    print ("Your Main Cost", t ,"\ntotal after tax(7%):",'$',round (totalT, 2))

hot_dog_order()

