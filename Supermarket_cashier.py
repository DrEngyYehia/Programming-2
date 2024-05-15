import sys


class Product:
    def __init__(self, product_ID, name, price, manufacturer, weight, expiration_date, year):
        self.supermarket_name = "AHMED SUPERMARKET"
        self.__product_ID = product_ID
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year
    def product_detail(self):
        print(f"Product Details:-\n"f"Super market name: {self.supermarket_name}\n"
              f"Product_ID: {self.__product_ID}\n"f"Name: {self.name}\n"f"Price: {self.price}\n"
              f"Manufacturer: {self.manufacturer}\n"f"Weight: {self.weight}\n"
              f"Expiration_date: {self.expiration_date}\n"
              f"year: {self.year}")
    def add_new_product(self):
        self.__product_ID = int(input("enter product_id : "))
        self.name = str(input("enter product name: "))
        self.price = float(input("enter product price: "))
        self.manufacturer = input("enter manufacturer of product: ")
        self.weight = float(input("enter weight of product: "))
        self.expiration_date = input("enter expiration_date of  product: ")
        self.year = int(input("enter year of production of product: "))
        print("******** NEW product has been added ******** \n"f"product_id : {self.__product_ID}\n"
              f"product name: {self.name}\n"f"product price: {self.price}\n"
              f" manufacturer of product: {self.manufacturer}\n"f"weight of product: {self.weight}\n"
              f"expiration_date of  product: {self.expiration_date}\n"f"year of product: {self.year}")
    def set_product_id(self, new_id):
        new_id = input("enter new product_ID: ")
        self.__product_ID = new_id

    def transaction(self):
        print('''
            TRANSACTION      
        **********************************************
            menu:
            1. Add new product
            2. Display product detail
            3. Change/edit product_ID
            4. Exit the sub-system
            5. Exit the Supermarket cashier system
        **********************************************
            ''')
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4, or 5 :"))
            except:
                print("Error:Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    self.add_new_product()
                elif option == 2:
                    self.product_detail()
                elif option == 3:
                    self.set_product_id(new_id="")
                elif option == 4:
                    break
                elif option == 5:
                    print("THANKS FOR CHOOSING AHMED SUPERMARKET")

                    sys.exit()
class Healthy(Product):
    def __init__(self, product_ID, name, price, manufacturer, weight, expiration_date,
                 year, components, calories=0):
        super().__init__(product_ID, name, price, manufacturer, weight, expiration_date,year)
        self.calories = calories
        self.components = components
    def Healthy_product_detail(self):
        print(f"Product Details:-\n"f"Super market name: {self.supermarket_name}\n"
              f"Product_ID: {self.__product_ID}\n"f"Name: {self.name}\n"f"Price: {self.price}\n"
              f"Manufacturer: {self.manufacturer}\n"f"Weight: {self.weight}\n"
              f"Expiration_date: {self.expiration_date}\n"
              f"year: {self.year}\n"f"calories: {self.calories}\n"f"components: {self.components}")

    def Add_new_Healthy_product(self):
        self.__product_ID = int(input("enter Healthy product_id : "))
        self.name = str(input("enter Healthy product name: "))
        self.price = int(input("enter Healthy product price: "))
        self.manufacturer = str(input("enter manufacturer of Healthy product: "))
        self.weight = float(input("enter weight of Healthy product per gram : "))
        self.expiration_date = input("enter expiration_date of Healthy product: ")
        self.year = int(input("enter year of production of Healthy product: "))
        self.calories = float(input("enter calories of Healthy product per gram : "))
        self.components = input("enter components of Healthy product : ")
        print("******** NEW Healthy product has been added ******** \n"f"Healthy product_id : {self.__product_ID}\n"
              f"Healthy product name: {self.name}\n"f"product price: {self.price}\n"
              f" manufacturer of Healthy product: {self.manufacturer}\n"
              f"weight of Healthy product: {self.weight}\n"
              f"expiration_date of Healthy product: {self.expiration_date}\n"
              f"year of Healthy product: {self.year}\n"f"calories: {self.calories}\n"f"components: {self.components}")
    def Change_calories(self):
        self.calories = float(input("enter new num of calories: "))
        print(f"Healthy product calories are: {self.calories}")
    def check_calories_components_healthy_product(self):
        print(f"calories of Healthy product are: {self.calories}\n"
              f"and components of Healthy product are: {self.components}")
    def tot_calories_of_healthy_product(self):
        total_calories = float((self.calories*self.weight))
        print(f"total calories of the Healthy product based on the weight (by gram)={total_calories} ")

    def transaction_of_healthy_product(self):
        print('''
            TRANSACTION      
        **********************************************
            menu:
            1. Add new Healthy product
            2. Display Healthy product detail
            3. Change/edit calories
            4. check calories and components of Healthy product
            5. compute total calories of the Healthy product based on weight
            6. Exit the sub-system
            7. Exit the supermarket cashier system 
        **********************************************
            ''')
        while True:
            try:
                option_2 = int(input("Enter 1, 2, 3, 4, 5, 6, or 7 ! :"))
            except:
                print("Error:Enter 1, 2, 3, 4, 5, 6, or 7 only!\n")
                continue
            else:
                if option_2 == 1:
                    self.Add_new_Healthy_product()
                elif option_2 == 2:
                    self.Healthy_product_detail()
                elif option_2 == 3:
                    self.Change_calories()
                elif option_2 == 4:
                    self.check_calories_components_healthy_product()
                elif option_2 == 5:
                    self.tot_calories_of_healthy_product()
                elif option_2 == 6:
                    break
                elif option_2 == 7:
                    print("THANKS FOR CHOOSING AHMED SUPERMARKET")

                    sys.exit()
print("******WELCOME TO AHMED SUPERMARKET*******")
print("____________________________________________________________________"
           "___________________________________\n")
print("__________OPTIONS__________")
product_obj = Product(product_ID="", name="", price="", manufacturer="", weight="", expiration_date="", year="")
Healthy_obj = Healthy(product_ID="", name="", price="", manufacturer="", weight="", expiration_date="", year=""
                      ,components="")
while True:
    try:
        trans = int(input("which sub-system you want to use: \n"
                      "1. Product system\n"
                      "2. Healthy system\n"
                      "3. Exit\n"))
    except:
        print("Error:Enter 1, 2, 3, only!\n")
        continue
    else:
     if trans == 1:
        product_obj.transaction()
     elif trans == 2:
        Healthy_obj.transaction_of_healthy_product()
     elif trans == 3:
        print('''
        ------------------------------------------
        | Thanks for choosing AHMED SUPERMAEKET  |
        | Visit us again!                        |
        ------------------------------------------ 
        ''')
        break
     else:
        print("Invalid number choose correct number")

