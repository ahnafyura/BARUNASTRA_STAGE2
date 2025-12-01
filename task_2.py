import abc
from abc import ABC, abstractmethod

class Product(ABC): 
    def __init__(self, product_name):
        self._product_name = product_name
    
    @property
    def name(self):
        return self._product_name
    
    @abstractmethod
    def get_info(self):
        pass

class Drink(Product):
    def __init__(self, product_name, volume_ml):
        super().__init__(product_name)
        self._volume_ml = volume_ml

    def get_info(self):
        return f"{self._volume_ml} ml"
        
class Snack(Product):
    def __init__(self, product_name, calories):
        super().__init__(product_name)
        self._calories = calories

    def get_info(self):
        return f"{self._calories} kcal"
    
class VendingMachine: 
    def __init__(self):
        self._product_list = []

    def add_product(self, product):
        self._product_list.append(product)
    
    def display_products(self):
        w_name = 20 
        w_info = 15
        pembatas = f"+{'-' * (w_name + 2)}+{'-' * (w_info + 2)}+"

        print("\n VENDING MACHINE ")
        print(pembatas)
        print(f"| {'Product Name':<{w_name}} | {'Information':>{w_info}} |")
        print(pembatas)

        total_mililiters = 0
        total_calories = 0

        for item in self._product_list:
            print(f"| {item.name:<{w_name}} | {item.get_info():>{w_info}} |")
            
            if isinstance(item, Drink):
                total_mililiters += item._volume_ml
            elif isinstance(item, Snack):
                total_calories += item._calories

        print(pembatas)
        print(f"| {'TOTAL Drink':<{w_name}} | {total_mililiters:>12} ml |")
        print(f"| {'TOTAL Snack':<{w_name}} | {total_calories:>10} kcal |")
        print(pembatas)
        print(" ")

if __name__ == "__main__":
    my_machine = VendingMachine()
    try:
        raw_n = input()
        if not raw_n:
            n = 0
        else:
            n = int(raw_n)
    except ValueError:
        print("Inputnya harus angka gng")
        exit()

    for _ in range(n):
        data = input().split() 
        
        if len(data) < 3:
            continue

        type_product = data[0]
        product_name = data[1]
        value = int(data[2])

        if type_product.lower() in ["drink", "d"]:
            item = Drink(product_name, value)
            my_machine.add_product(item)
            
        elif type_product.lower() in ["snack", "s"]:
            item = Snack(product_name, value)
            my_machine.add_product(item)
            
        else:
            print(f"⚠ Tipe '{type_product}' tipenya ngga ada deh, aku skip ya.")

    my_machine.display_products()
