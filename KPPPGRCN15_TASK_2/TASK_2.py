import abc
from abc import ABC, abstractmethod

class Product(ABC): 
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def get_info(self):
        pass

class Drink(Product):
    def __init__(self, name, volume_ml):
        super().__init__(name)
        self._volume_ml = volume_ml

    def get_info(self):
        return f"{self._volume_ml} ml"
        
class Snack(Product):
    def __init__(self, name, calories):
        super().__init__(name)
        self._calories = calories

    def get_info(self):
        return f"{self._calories} kcal"
    
class VendingMachine: 
    def __init__(self):
        self._listProducts = []

    def add_product(self, product):
        self._listProducts.append(product)
    
    def display_products(self):
        total_mililiters = 0
        total_calories = 0
        print("")
        for item in self._listProducts:
            print(f"{item.name}: {item.get_info()}")
            
            if isinstance(item, Drink):
                total_mililiters += item._volume_ml
            elif isinstance(item, Snack):
                total_calories += item._calories
        print("")
        print(f"Total drink: {total_mililiters} ml")
        print(f"Total snack: {total_calories} kcal")

if __name__ == "__main__":
    my_machine = VendingMachine()
    
    try:
        raw_n = input()
        if not raw_n:
            exit()
        n = int(raw_n)
    except ValueError:
        exit()

    for _ in range(n):
        try:
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
        except ValueError:
            continue
    my_machine.display_products()