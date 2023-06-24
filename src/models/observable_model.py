class Event:
    def __init__(self) -> None:
        self.observers = {}

    def notify(self, event, *args, **kwargs):
        self.observers[event](*args, **kwargs)

    def add_event_listener(self, event, fn):
        self.observers[event] = fn

    def detach(self, observer):
        try:
            self.observers.pop(observer)
        except ValueError:
            pass
