class Item:
    def __init__(self, name, stackable=True, maxStack=100):
        self.name = name
        self.stackable = stackable
        self.maxStack = maxStack