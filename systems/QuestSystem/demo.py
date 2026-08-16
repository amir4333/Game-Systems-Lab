from Quest import Quest
from QuestObjective import QuestObjective
from QuestSystem import QuestSystem


# -------------------------
# Create Objectives
# -------------------------

collect_apples = QuestObjective(
    "Collect apples",
    3
)

talk_to_farmer = QuestObjective(
    "Talk to the farmer",
    1
)


# -------------------------
# Create Quest
# -------------------------

farmer_quest = Quest(
    "Help the Farmer",
    "Help the farmer prepare his apples.",
    [
        collect_apples,
        talk_to_farmer
    ]
)


# -------------------------
# Create another Quest
# -------------------------

find_sword = QuestObjective(
    "Find the lost sword",
    1
)

sword_quest = Quest(
    "Find the Sword",
    "Find the sword that was lost near the forest.",
    [
        find_sword
    ]
)


# -------------------------
# Create Quest System
# -------------------------

quest_system = QuestSystem([])


# -------------------------
# Start Quests
# -------------------------

quest_system.add_quest(farmer_quest)
quest_system.add_quest(sword_quest)


# -------------------------
# Check active quests
# -------------------------

print("Active quests:")

for quest in quest_system.active_quests:
    print("-", quest.name)


# -------------------------
# Progress Farmer Quest
# -------------------------

collect_apples.add_progress()
collect_apples.add_progress()
collect_apples.add_progress()

talk_to_farmer.add_progress()


# -------------------------
# Update Quest System
# -------------------------

quest_system.update()


# -------------------------
# Check results
# -------------------------

print("\nActive quests:")

for quest in quest_system.active_quests:
    print("-", quest.name)

print("\nCompleted quests:")

for quest in quest_system.completed_quests:
    print("-", quest.name)