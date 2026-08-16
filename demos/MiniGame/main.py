from systems.InventorySystem.Inventory import Inventory
from systems.InventorySystem.Item import Item
from systems.QuestSystem.QuestObjective import QuestObjective
from systems.QuestSystem.QuestSystem import QuestSystem
from systems.QuestSystem.Quest import Quest
from systems.DialogueSystem.DialogueSystem import DialogueSystem
from systems.DialogueSystem.DialogueChoice import DialogueChoice
from systems.DialogueSystem.DialogueNode import DialogueNode

inventory = Inventory([])
quest_system = QuestSystem([])

#-------------------------------------------------------------------
# Dialogues

print("You are standing in front of the city gate.")

# End node
goodbye_node = DialogueNode(
    "Goodbye, traveler.",
    []
)

# Accepting quest
accept_quest = DialogueSystem(
    "Thank you. Bring it back to me when you find it.",
    []
)

guard_continius = DialogueSystem(
    "My sword was stolen and I think the thief took it into the forest.",
    [
        DialogueChoice("I'll find it.",),
        DialogueChoice("Maybe later.",goodbye_node)
    ]
)

start_node = DialogueSystem(
    "Hey! You there. I need your help.",
    [
        DialogueChoice("I can help. What happened?",guard_continius),
        DialogueChoice("Sorry, I'm busy.",goodbye_node)
    ]
)

dialogue = DialogueSystem(start_node)

#------------------------------------------------------------------------
# Creating quest

# -------------------------
# Create Objectives
# -------------------------

Find_the_Lost_Sword = QuestObjective(
    "Talk to the farmer",
    1
)


# -------------------------
# Create Quest
# -------------------------

farmer_quest = Quest(
    "The Lost Sword",
    "Find the guard's lost sword and bring it back.",
    [
        Find_the_Lost_Sword
    ]
)

