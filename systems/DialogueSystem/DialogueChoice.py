class DialogueChoice:
    
    def __init__(self, text, next_node, action=None):
        self.text = text
        self.next_node = next_node
        self.action = action