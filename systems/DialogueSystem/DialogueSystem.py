class DialogueSystem:
    
    def __init__(self, start_node):
        self.start_node = start_node
        self.current_node = start_node

        # self.second_choices = [DialogueChoice("Goodbye.")]
        # self.start_choices = [DialogueChoice("Who are you?", DialogueNode("I am the city guard.", self.second_choices)), DialogueChoice("Goodbye.")]
        # self.current_node = DialogueNode("Hello", self.start_choices)

    def Go_to_next_node(self, choice_index):
        if len(self.current_node.choices) != 0:
            self.current_node = self.current_node.choices[choice_index].next_node

        if len(self.dialogue_node.choices) == 0:
            self.End_dialogues()

    def End_dialogues(self):
        pass