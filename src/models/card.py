class Card:
    def __init__(self, iid, question, answer, created_at, deck_id) -> None:
        self._iid = iid
        self._question = question
        self._answer = answer
        self._created_at = created_at
        self._deck_id = deck_id

    @property
    def iid(self):
        return self._iid

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer

    @property
    def deck_id(self):
        return self._deck_id

    @property
    def created_at(self):
        return self._created_at
