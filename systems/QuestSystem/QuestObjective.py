class QuestObjective:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        self.progress = 0

    def add_progress(self):
        self.progress += 1

    def is_completed(self):
        if self.progress >= self.amount:
            return True
        return False