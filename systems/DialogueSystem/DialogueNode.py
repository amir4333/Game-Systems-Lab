from DialogueSystem import DialogueSystem
class DialogueNode:

    def __init__(self, text, choices):
        self.text = text
        self.choices = choices

        self.dialogue_system = DialogueSystem(self.text)