class QuestSystem:
    def __init__(self, active_quests):
        self.active_quests = active_quests

    def add_quest(self, quest):
        if quest not in self.active_quests:
            self.active_quests.append(quest)
            return

    def remove_quest(self, quest):
        if quest in self.active_quests:
            self.active_quests.remove(quest)
            return

    def update(self):
        for quest in (self.active_quests):
            if quest.is_complete():
                self.remove_quest(quest)
