class Supply:
    pass

# Initializer / Instance Attributes
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def get_price (self):
        return self.cost * 2.5

class Pen(Supply):

    def set_color(self):
        self.special_color = "Blue"
    def get_color(self):
        return self.special_color

if (__name__ == '__main__'):
    print('Executing as standalone script')
    
    supply1 = Supply("Dog Food", 10)
    supply2 = Supply("Cat Food", 15)
    supply3 = Pen("Bic Pens", 1)
    supply4 = Supply("Script", 4)
    pen1 = Pen("Script", 4)
    supply3.set_color()
    pen1.set_color()
    print(supply1.brand)
    print(supply2.brand)
    print(supply1.get_price())
    print(supply3.get_color())
    print(supply3.brand)
    print(supply3.cost)
    print(supply3.get_price())
    print(pen1.get_color())