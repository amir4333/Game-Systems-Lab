class ItemDefinition:
    def __init__(self, id, name, stackable=True, max_stack=100, max_durability=1):
        self.id = id
        self.name = name
        self.stackable = stackable
        self.max_stack = max_stack
        self.max_durability = max_durability