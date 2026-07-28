from InventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []
    
    def add_item(self, item, quantity=1):
        slot = self.get_slot(item)
        if slot is not None:
            slot.quantity += quantity
            return
        self.slots.append(InventorySlot(item, quantity))

    def remove_item(self, item, count=1): 
        slot = self.get_slot(item)
        if slot is not None:
            slot.quantity -= count
            if slot.quantity <= 0:
                self.slots.remove(slot)
            return True
        return False

    def get_slot(self, item):
        for slot in self.slots: 
            if slot.item.name == item.name:
                return slot
        return None
