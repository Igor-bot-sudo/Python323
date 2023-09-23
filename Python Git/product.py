class Product:

    def __init__(self, name: str, cost: float, type_: str):
        self.name = name
        self.cost = cost
        self.type_ = type_

    def update_cost(self, cost):
        if cost < 0:
            return
        self.cost = cost
    
    def product_price(self, weight):
        return self.cost * weight


cucumbers = Product('cucumber', 75.0, 'vegetables')
weight = float(input('Вес товара: ')) # 2.75 = 2 kilograms and 750 grams
print(cucumbers.product_price(weight))
