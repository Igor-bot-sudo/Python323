class Product:

    def __init__(self, name, cost, type):
        self.name = name
        self.cost = cost
        self.type = type

    def update_cost(self, cost):
        if cost < 0:
            return
        self.cost = cost
