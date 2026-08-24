from systems.InventorySystem.Inventory import Inventory
from systems.InventorySystem.Item import Item
from systems.QuestSystem.QuestObjective import QuestObjective
from systems.QuestSystem.QuestSystem import QuestSystem
from systems.QuestSystem.Quest import Quest
from systems.DialogueSystem.DialogueSystem import DialogueSystem
from systems.DialogueSystem.DialogueChoice import DialogueChoice
from systems.DialogueSystem.DialogueNode import DialogueNode
from systems.EventSystem.EventSystem import EventSystem


#------------------------------------------------------------- Contents --------------------------------------------------------------

ITEM_ADDED = "item_added"


# -------------------------
# Objectives
# -------------------------

find_lost_sword = QuestObjective(
    "Find the Lost Sword",
    1
)


# -------------------------
# Quest
# -------------------------

lost_sword_quest = Quest(
    "The Lost Sword",
    "Find the guard's lost sword and bring it back.",
    [
        find_lost_sword
    ]
)


#-------------------------------------------------------------------------------------------------------------------------------------

# Items
sword = Item("sword", False)


#-------------------------------------------------------------------------------------------------------------------------------------
# Functions

def start_quest(quest):
    input("> quest started!")

    quest_system.add_quest(quest)

def explore():
    input("> explore")
    input("> you found an item!")
    input("> its a sword!")

    inventory.add_item(sword)

    event_system.emit(
        ITEM_ADDED,
        {
            "count": 1
        }
    )

def end_quest():
    quest_system.update()

    input("> quest ended.(push any button)")

def show_quests():
    print("\n========== QUESTS ==========")

    print("\nActive Quests:")
    if not quest_system.active_quests:
        print("  No active quests.")
    else:
        for quest in quest_system.active_quests:
            print(f"  - {quest.name}")

    print("\nCompleted Quests:")
    if not quest_system.completed_quests:
        print("  No completed quests.")
    else:
        for quest in quest_system.completed_quests:
            print(f"  - {quest.name}")

    print("\n============================")

#-------------------------------------------------------------------------------------------------------------------------------------

# Dialogues

print("You are standing in front of the city gate.")

# End node
goodbye_node = DialogueNode(
    "Goodbye, traveler.",
    []
)

# Accepting quest
accept_quest = DialogueNode(
    "Thank you. Bring it back to me when you find it.",
    []
)

# Start quest dialogue
guard_continius = DialogueNode(
    "My sword was stolen and I think the thief took it into the forest.",
    [
        DialogueChoice("I'll find it.", accept_quest),
        DialogueChoice("Maybe later.", goodbye_node)
    ]
)

# Start node
start_node = DialogueNode(
    "Hey! You there. I need your help.",
    [
        DialogueChoice("I can help. What happened?",guard_continius),
        DialogueChoice("Sorry, I'm busy.",goodbye_node)
    ]
)


#------------------------------------------------------------- States ----------------------------------------------------------------

inventory = Inventory([])
quest_system = QuestSystem([])
dialogue = DialogueSystem(start_node)
event_system = EventSystem()

#------------------------------------------------------------- Events ----------------------------------------------------------------

event_system.subscribe(item_adDEDded, find_lost_sword.add_progress)

#------------------------------------------------------------- Brain -----------------------------------------------------------------

# Dialogues
def dialogue_while():
    while True:

        print("\n" + dialogue.current_node.text)

        if dialogue.is_finished():
            break

        for i, choice in enumerate(dialogue.current_node.choices):
            print(f"{i}: {choice.text}")

        answered_right = False
        while not answered_right:
            selected = int(input("> "))
            
            if 0 <= selected < len(dialogue.current_node.choices):
                dialogue.choose(selected)
                answered_right = True
            else:
                print("Invalid choice")


#------------------------------------------------------------- Main ------------------------------------------------------------------

show_quests()
dialogue_while()

start_quest(lost_sword_quest)
show_quests()

explore()
end_quest()
show_quests()