from DialogueNode import DialogueNode
from DialogueChoice import DialogueChoice
from DialogueSystem import DialogueSystem


# End node
goodbye_node = DialogueNode(
    "Goodbye, traveler.",
    []
)


# Guard answer node
guard_node = DialogueNode(
    "I am the city guard. I protect this town.",
    [
        DialogueChoice(
            "Goodbye.",
            goodbye_node
        )
    ]
)


# First node
start_node = DialogueNode(
    "Hello traveler! What do you need?",
    [
        DialogueChoice(
            "Who are you?",
            guard_node
        ),

        DialogueChoice(
            "Goodbye.",
            goodbye_node
        )
    ]
)


# Create dialogue system
dialogue = DialogueSystem(start_node)


# Testing
print(dialogue.current_node.text)

for index, choice in enumerate(dialogue.current_node.choices):
    print(index, choice.text)


# Player chooses first option
dialogue.choose(0)

print("\nAfter choosing:")
print(dialogue.current_node.text)