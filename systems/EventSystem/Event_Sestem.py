class EventSystem:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, eventName, listener):
        self.listeners.update({eventName: listener})

    def unsubscrobe(self, eventName, listener):
        self.listeners.popitem({{eventName: listener}})

    def emit(self, eventName, data):
        pass