class EventSystem:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, eventName, listener):
        if eventName in self.listeners:
            if listener not in self.listeners[eventName]:
                self.listeners[eventName].append(listener)
                return
        
        self.listeners.update({eventName: [listener]})

    def unsubscribe(self, eventName, listener):
        if eventName in self.listeners:
            if listener in self.listeners[eventName]:
                self.listeners[eventName].remove(listener)

    def emit(self, eventName, data):
        if eventName in self.listeners:
            for listener in self.listeners[eventName]:
                listener(data)