print("                 Gawde Supershop                ")
print("Assalamualaikum 😀")
print("For Electronics Section Type Electronics \n For Clothing Section Type 'Clothings' \n For Groceries Type Groceries \n Type exit to quit ")
print("There'll be no problem if you type it in small or capital letter")

def display_electronics():
    laptops = [
        {'Brand': 'HP', 'Model': 'Spectre', 'Price': 1500, 'ProductNumber': 'HP001', 'Quantity' : 150},
        {'Brand': 'HP', 'Model': 'Pavilion', 'Price': 1000, 'ProductNumber': 'HP002', 'Quantity' : 200},
        {'Brand': 'Asus', 'Model': 'ROG', 'Price': 2000, 'ProductNumber': 'AS001', 'Quantity' : 480},
        {'Brand': 'Asus', 'Model': 'VivoBook', 'Price': 800, 'ProductNumber': 'AS002', 'Quantity' : 300},
        {'Brand': 'Apple', 'Model': 'MacBook Air', 'Price': 1200, 'ProductNumber': 'AP001', 'Quantity' : 500},
        {'Brand': 'Apple', 'Model': 'MacBook Pro', 'Price': 2500, 'ProductNumber': 'AP002', 'Quantity' : 250}
    ]
    mobiles = [
        {'Brand': 'Samsung', 'Model': 'Galaxy S21', 'Price': 999, 'ProductNumber': 'SS001', 'Quantity' : 450},
        {'Brand': 'Samsung', 'Model': 'Galaxy A52', 'Price': 499, 'ProductNumber': 'SS002', 'Quantity' : 550},
        {'Brand': 'Apple', 'Model': 'iPhone 16', 'Price': 1099, 'ProductNumber': 'IP001', 'Quantity' : 350},
        {'Brand': 'Apple', 'Model': 'iPhone 15 Pro Max', 'Price': 899, 'ProductNumber': 'IP002', 'Quantity' :250},
        {'Brand': 'OnePlus', 'Model': '9 Pro', 'Price': 899, 'ProductNumber': 'OP001', 'Quantity' : 500},
        {'Brand': 'OnePlus', 'Model': 'Nord', 'Price': 499, 'ProductNumber': 'OP002', 'Quantity' : 700}
    ]
    Electronic_Section = laptops + mobiles
    print("Elcetronics Section: ")
    for Electronics in Electronic_Section:
        brand = Electronics['Brand']
        model = Electronics['Model']
        price = Electronics['Price']
        product_num = Electronics['ProductNumber']
        print(f"Brand: {brand}, Model: {model}, Price: {price} USD, Product number: {product_num}")
    return Electronic_Section

def display_Clothings():
        
    clothing = [{'Type': 'Tshirt', 'Price': 100, 'ProductNumber': 'TS54', 'Quantity': 800},
                {'Type': 'Shirt', 'Price': 100, 'ProductNumber': 'Sh64', 'Quantity': 800},
                {'Type': 'Jeans', 'Price': 130, 'ProductNumber': 'Jns50', 'Quantity': 800},
                {'Type': 'Joggers', 'Price': 110, 'ProductNumber': 'JGRS24', 'Quantity': 800}]

    print("Clothing Section: ")
    for cloths in clothing:
        type = cloths['Type']
        price = cloths['Price']
        product_num = cloths['ProductNumber']
        print(f"Type: {type}, Price: {price} USD, Product number: {product_num}")
    return clothing

def display_Grocery():
    Grocery = [{'Item' : 'Rice', 'Price' : 20, 'Kilo' : 2000},
            {'Item' : 'Beef', 'Price' : 45, 'Kilo' : 6000},
            {'Item' : 'Meat', 'Price' : 32, 'Kilo' : 4750},
            ]

    print("Grocery Section: ")
    for items in Grocery:
        item = items['Item']
        price = items['Price']
        kilo = items['Kilo']
        print(f"Item: {item}, price: {price} USD, Kilo: {kilo}")
    return Grocery


def buy_product():
        sections = display_electronics() + display_Clothings() + display_Grocery()  
        while True:
            customer = input("What would you like to buy?: ")
        
            if customer.lower() == 'exit':
                print("Exiting the purchase process.")
                break
            if customer.capitalize() == 'Electronics':
                product_found = False 
                product_num = input("Please Enter Product Number: ")
                for product in sections:
                    if product_num == product['ProductNumber']:  
                        product_found = True 
                        confirm = input(f"Do you want to purchase Brand: {product['Brand']}, Model: {product['Model']}, Price: {product['Price']} USD? (yes/no): ").lower()
                        if confirm == 'yes':
                            print("Product Purchased Successfully")
                            print("Thanks for buying 😊")
                        elif confirm == 'no':
                            print("Purchase Cancelled")
                        break 
                
                if not product_found:  
                    print("Product number not found. Please try again.")
            if customer.capitalize() == 'Clothings':
                product_found = False
                product_num = input("Please Enter Product Number: ")
                for product in sections:
                    if product_num == product['ProductNumber']:  
                        product_found = True 
                        confirm = input(f"Do you want to purchase Type: {product['Type']}, Price: {product['Price']}USD? (yes/no)")
                        if confirm == 'yes':
                            print("Product Purchased Successfully")
                            print("Thanks for buying 😊")
                        elif confirm == 'no':
                            print("Purchase Cancelled")
                        break 
            elif customer.capitalize() == 'Groceries':
                product_found = False
                buy_item = input("Which item would you like to buy? ")
                buy_kilo = int(input("How many kilos? "))
                for product in sections:
                    if 'Item' in product: 
                        item_buy = product['Item']
                        kilo_buy = product['Kilo']
                        if buy_item.lower() == item_buy.lower() and buy_kilo <= kilo_buy:  
                            product_found = True
                            print(f"Item: {item_buy}, Kilo: {buy_kilo}")
                            confirm = input("Type 'yes' to confirm and 'no' to cancel: ").lower()
                            if confirm == 'yes':
                                print("Product Purchased Successfully")
                                print("Thanks for buying 😊")
                            elif confirm == 'no':
                                print("Purchase Cancelled")
                            break  
                
                if not product_found:
                    print("Item not found or insufficient quantity. Please try again.")
                
buy_product()
