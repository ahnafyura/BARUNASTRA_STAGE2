import abc
from abc import ABC, abstractmethod

class Product(ABC): 
    def __init__(self, ProductName):
        self._ProductName = ProductName
    
    @property
    def Name(self):
        return self._ProductName
    
    @abstractmethod
    def get_info(self):
        pass

class Drink(Product):
    def __init__(self, ProductName, Mililiters):
        super().__init__(ProductName)
        self._Mililiters = Mililiters

    def get_info(self):
        return f"{self._Mililiters} ml"
        
class Snack(Product):
    def __init__(self, ProductName, Calories):
        super().__init__(ProductName)
        self._Calories = Calories

    def get_info(self):
        return f"{self._Calories} kcal"
    
class VindingMachine:
    def __init__(self):
        self._Product = []

    def addProduct(self, Product):
        self._Product.append(Product)
    
    def Display(self):
        w_name = 20 
        w_info = 15
        
        pembatas = f"+{'-' * (w_name + 2)}+{'-' * (w_info + 2)}+"

        print(pembatas)
        print(f"| {'Product Name':<{w_name}} | {'Information':>{w_info}} |")
        print(pembatas)

        total_mililiters = 0
        total_calories = 0

        for item in self._Product:
            print(f"| {item.Name:<{w_name}} | {item.get_info():>{w_info}} |")
            
            if isinstance(item, Drink):
                total_mililiters += item._Mililiters
            elif isinstance(item, Snack):
                total_calories += item._Calories

        print(pembatas)
        print(f"| {'TOTAL Drink':<{w_name}} | {total_mililiters:>12} ml |")
        print(f"| {'TOTAL Snack':<{w_name}} | {total_calories:>10} kcal |")
        print(pembatas)
        print(" ")

if __name__ == "__main__":
    Vinding_Machine = VindingMachine()
    
    n = int(input())

    for _ in range(n):
        data = input().split() 

        TypeProduct = data[0]
        ProductName = data[1]
        value = int(data[2])

        if TypeProduct == "Drink" or TypeProduct == "drink":
            drinkItem = Drink(ProductName, value)
            Vinding_Machine.addProduct(drinkItem)
        elif TypeProduct == "Snack" or TypeProduct == "Snack":
            SnackItem = Snack(ProductName, value)
            Vinding_Machine.addProduct(SnackItem)
        else:
            print(f"Tipe '{TypeProduct}' pada produk '{ProductName}' tidak dikenali. Produk dilewati")

    Vinding_Machine.Display()