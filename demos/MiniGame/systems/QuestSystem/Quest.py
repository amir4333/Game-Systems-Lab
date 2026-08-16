class Quest:
    def __init__(self, name, description, objectives):
        self.name = name
        self.description = description
        self.objectives = objectives

    def is_complete(self):
        for objective in self.objectives:
            if not objective.is_complete():
                return False
        return True