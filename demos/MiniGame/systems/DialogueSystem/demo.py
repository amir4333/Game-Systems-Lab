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
while True:

    print("\n" + dialogue.current_node.text)

    if dialogue.is_finished():
        break

    for i, choice in enumerate(dialogue.current_node.choices):
        print(f"{i}: {choice.text}")

    choosed_correct = False
    while not choosed_correct:
        selected = int(input("> "))
        
        if 0 <= selected < len(dialogue.current_node.choices):
            dialogue.choose(selected)
            choosed_correct = True
        else:
            print("Invalid choice")