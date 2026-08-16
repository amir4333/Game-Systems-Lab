class QuestSystem:
    def __init__(self, active_quests):
        self.active_quests = active_quests
        self.completed_quests = []
        self.all_quests = set()

    def add_quest(self, quest):
        if quest in self.all_quests:
            return
        self.all_quests.add(quest)
        self.active_quests.append(quest)

    def remove_quest(self, quest):
        if quest in self.active_quests:
            self.active_quests.remove(quest)

    def send_to_completed(self, quest):
        if quest in self.active_quests:
                self.active_quests.remove(quest)
                self.completed_quests.append(quest)

    def update(self):
        for quest in self.active_quests[:]:
            if quest.is_complete():
                self.send_to_completed(quest)