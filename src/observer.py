class Subject:
    def __init__(self) -> None:
        self._observers = []

    def notify(self, *args):
        for observer in self._observers:
            observer.update(*args)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
