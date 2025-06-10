stock = {}
print("------Welcome To Fruit Market------")
print("Press 1 for Manager")
print("Press 2 for Customer")
print("Press 3 for Exist")
role = int(input("Enter Your Role: "))
    


if role ==1:
 while True:

        print("1. Add Fruit Stock")
        print("2. View Stock")
        print("3. Update Stock")
        print("4. Exist")
        

        menu = int(input("Enter Your Choice what you can do: "))
        if menu ==1:
            def add_stock():
                fruit = input("Enter Fruit Name to add: ").capitalize()
                quantity = int(input("Enter quantity in  Kg : "))
                price = int(input("Enter price for (in kg): "))

                if fruit in stock:
                    stock[fruit] ['quantity'] += quantity
                    stock[fruit] ['price'] = price

                else:
                    stock[fruit] = {'quantity in kg' : quantity, 'price': price}

                print(f"{'quantity'} kg of {'fruit'} added to our stock.")

            add_stock()

                    
            choice1 = input("Enter Y or N: ")
            if choice1 == "Y":
                menu = int(input("Enter your choice: "))
                print(menu)

            elif choice1 == "N":
                print("Thank You For Visiting Fruit Market")
                exit()

            else:
                 print("Invalid Input Please Enter Y or N")
                    

        elif menu == 2:
               def view_stock():
                    if not stock:
                        print("Stock is Empty")

                    else:
                        print("Current Fruit Stock:")
                        print(stock, "in kg")

               view_stock()

        elif menu == 3:
              def update_stock():
                    fruit = input("Enter Fruit name to update: ").capitalize()
                    if fruit in stock:
                        print(f"Current Details of {fruit}: quantity = {stock[fruit]['quantity in kg']} kg, price = {stock[fruit]['price']} per kg")
                        new_quantity = int(input(f"Enter new quantity for {fruit}: "))
                        new_price = int(input("Enter new price for {fruit}: "))

                        stock[fruit]['quantity'] = new_quantity
                        stock[fruit]['fruit'] = new_price

                        print(f"{fruit} stock Updated Succesfully")

                    else:
                        print(f"{fruit} not found in stock")


              update_stock()

        else:
             menu == 4
             print("Thank You for Visiting Fruit Martket")
             break
        

else:
     role == 3
     print("Thank You for Visiting")
     
   