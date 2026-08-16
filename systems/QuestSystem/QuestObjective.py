class QuestObjective:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        self.progress = 0

    def add_progress(self, amount=1):
        self.progress += amount

    def is_complete(self):
        return self.progress >= self.amount