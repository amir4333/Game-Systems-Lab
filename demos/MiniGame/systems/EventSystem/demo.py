from EventSystem import EventSystem

event_system = EventSystem()


def inventory_listener(data):
    print(f"[Inventory] Added {data['item']}")


def ui_listener(data):
    print(f"[UI] Show notification: {data['item']} added!")


def quest_listener(data):
    print(f"[Quest] Check quests for {data['item']}")


event_system.subscribe("item_added", inventory_listener)
event_system.subscribe("item_added", ui_listener)
event_system.subscribe("item_added", quest_listener)

event_system.emit(
    "item_added",
    {
        "item": "Sword"
    }
)