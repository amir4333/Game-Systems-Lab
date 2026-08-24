class DialogueSystem:

    def __init__(self, start_node):
        self.start_node = start_node
        self.current_node = start_node

    def choose(self, choice_index):
        if len(self.current_node.choices) != 0:
            choice = self.current_node.choices[choice_index]
            if choice.action:
                choice.action()
            self.current_node = self.current_node.choices[choice_index].next_node

    def is_finished(self):
        return len(self.current_node.choices) == 0