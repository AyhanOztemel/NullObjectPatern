from abc import ABC, abstractmethod

# Abstract Product Class
class Product:
    @abstractmethod
    def render(self):
        print("Product render method called.")

# Concrete Product  Class-1
class Windows(Product):
    def render(self):
        print("Windows render method called.")

# Concrete Product Class-2
class Mac(Product):
    def render(self):
        print("Mac render method called.")

# Factory Class
class FactoryClass:
    def create_product(self, Product):
        return Product()
        

# Example
factory = FactoryClass()

factoryProduct = factory.create_product(Windows)
factoryProduct.render()  # Windows  render method called.

factoryProduct = factory.create_product(Mac)
factoryProduct.render()  # Mac  render method called.
