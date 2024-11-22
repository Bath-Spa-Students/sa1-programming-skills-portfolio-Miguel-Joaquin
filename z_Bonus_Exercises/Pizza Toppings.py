# Pizza Toppings

Topping_Count = 0
Max_Toppings = 5

while Topping_Count < Max_Toppings:
    Topping = input(f"Enter Topping {Topping_Count + 1} of {Max_Toppings}: ")
    print(f"Great, we will add {Topping} on your pizza.")
    Topping_Count += 1

print("Maxium number of pizza topping has been reached")
