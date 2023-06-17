class Event:
    def __init__(self) -> None:
        self._observers = []

    def _get(self, name):
        for observer in self._observers:
            if observer["name"] == name:
                return observer["observer"]

    def notify(self, event, *args, **kwargs):
        for observer in self._observers:
            observer(*args, **kwargs)

    def add_event_listener(self, event, fn):
        if event not in self._observers:
            self._observers.append(fn)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
