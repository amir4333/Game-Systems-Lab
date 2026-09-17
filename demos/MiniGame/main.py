from functools import partial
from systems.InventorySystem.Inventory import Inventory
from systems.InventorySystem.Item import Item
from systems.QuestSystem.QuestObjective import QuestObjective
from systems.QuestSystem.QuestSystem import QuestSystem
from systems.QuestSystem.Quest import Quest
from systems.DialogueSystem.DialogueSystem import DialogueSystem
from systems.DialogueSystem.DialogueChoice import DialogueChoice
from systems.DialogueSystem.DialogueNode import DialogueNode
from systems.EventSystem.EventSystem import EventSystem

#------------------------------------------------------------- States ----------------------------------------------------------------

inventory = Inventory()
quest_system = QuestSystem([])
event_system = EventSystem()

#------------------------------------------------------------- Contents --------------------------------------------------------------

EXPLORE_ENDED = "explore_ended"
START_QUEST = "start_quest"


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
apple = Item("apple")

#-------------------------------------------------------------------------------------------------------------------------------------
# Functions

def start_quest(quest):
    event_system.emit(
        START_QUEST,
        {
            "quest": quest
        }
    )

    input("> quest started!")

def explore():
    input("\n> explore")

    print("\nYou walk into the forest...")
    input("Press Enter to continue...")

    print("\nYou found: Sword")

    event_system.emit(
        EXPLORE_ENDED,
        {
            "item": sword,
            "count": 1
        }
    )

def end_quest():
    quest_system.update()

    print("\nQuest completed!")
    print(f"  {lost_sword_quest.name}")

    input("\nPress Enter to continue...")

def show_quests():
    print("\n========== QUEST LOG ==========")

    print("\nActive:")
    if not quest_system.active_quests:
        print("  None")
    else:
        for quest in quest_system.active_quests:
            print(f"  [ ] {quest.name}")
            print(f"      {quest.description}")

    print("\nCompleted:")
    if not quest_system.completed_quests:
        print("  None")
    else:
        for quest in quest_system.completed_quests:
            print(f"  [✓] {quest.name}")

    print("\n===============================")

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
        DialogueChoice("I'll find it.", accept_quest, partial(start_quest, lost_sword_quest)),
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

dialogue = DialogueSystem(start_node)

#------------------------------------------------------------- Listener --------------------------------------------------------------

def inventory_listener(data):
    inventory.add_item(data["item"], data["count"])

def quest_listener(data):
    if data["item"] == sword:
        find_lost_sword.add_progress()

        print("\nObjective updated!")
        print(f"  Find the Lost Sword [{find_lost_sword.progress}/{find_lost_sword.amount}]")

def quest_start_listener(data):
    if data["quest"] == lost_sword_quest:
        quest_system.add_quest(data["quest"])


#------------------------------------------------------------- Events ----------------------------------------------------------------

event_system.subscribe(EXPLORE_ENDED, inventory_listener)
event_system.subscribe(EXPLORE_ENDED, quest_listener)

event_system.subscribe(START_QUEST, quest_start_listener)


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


dialogue_while()
show_quests()

explore()

end_quest()
show_quests()