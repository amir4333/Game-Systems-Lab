from DialogueChoice import DialogueChoice
from DialogueNode import DialogueNode

class DialogueSystem:
    def __init__(self):
        self.start_node

        self.second_choices = [DialogueChoice("Goodbye.")]
        self.start_choices = [DialogueChoice("Who are you?", DialogueNode("I am the city guard.", self.second_choices)), DialogueChoice("Goodbye.")]
        self.current_node = DialogueNode("Hello", self.start_choices)

    def Player_choice(self):
        pass

    def Go_to_next_node(self):

        if len(self.dialogue_node.choices) != 0:
            pass

        if len(self.dialogue_node.choices) == 0:
            self.End_dialogues()

    def End_dialogues(self):
        pass