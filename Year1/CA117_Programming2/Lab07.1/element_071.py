class Element(object):
    def __init__(self, number, name, symbol, boiling_point):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.boiling_point = boiling_point

    def print_details(self):
        l = []
        print("Number:", self.number)
        print("Name:", self.name)
        print("Symbol:", self.symbol)
        print("Boiling point:", self.boiling_point, "K")
