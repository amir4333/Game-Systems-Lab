from .InventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []
    
    def add_item(self, item_definition, quantity=1):
        slot = self.get_available_slot(item_definition)
        if slot is not None:
            if (slot.quantity + quantity) <= item_definition.max_stack:
                slot.quantity += quantity
            else:
                extra = quantity - (item_definition.max_stack - slot.quantity)
                slot.quantity += quantity - extra
                while extra > item_definition.max_stack:
                    self.slots.append(InventorySlot(item_definition, item_definition.max_stack))
                    extra -= item_definition.max_stack
                if extra:
                    self.slots.append(InventorySlot(item_definition, extra))
            return
        self.slots.append(InventorySlot(item_definition, quantity))

    def remove_item(self, item_definition, count=1): 
        slot = self.get_slot(item_definition)
        if slot is not None:

            if count < slot.quantity:
                slot.quantity -= count
                return count
            
            extra = count - slot.quantity
            slot.quantity -= (count - extra)
            self.slots.remove(slot)

            slot = self.get_slot(item_definition)
            while extra > 0:
                extra -= slot.quantity
                self.slots.remove(slot)
                slot = self.get_slot(item_definition)
                if slot is None:
                    return count - extra
            return count
        return 0

    def get_slot(self, item_definition):
        for slot in self.slots: 
            if slot.item_definition.id == item_definition.id:
                return slot
        return None

    def get_available_slot(self, item_definition):
        for slot in self.slots: 
            if slot.item_definition.id == item_definition.id:
                if slot.quantity < item_definition.max_stack:
                    return slot
        return None