class Event:
    def __init__(self) -> None:
        self._observers = []

    def _get(self, name):
        for observer in self._observers:
            if observer["name"] == name:
                return observer["observer"]

    def notify(self, message_type: str, receiver_name=None, *args, **kargs):
        if receiver_name:
            receiver = self._get(receiver_name)
            receiver.update(message_type, *args, **kargs)
        else:
            for observer in self._observers:
                observer.update(message_type, receiver_name, *args, **kargs)

    def attach(self, name, observer):
        if observer not in self._observers:
            self._observers.append({"name": name, "observer": observer})

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
