class Card:
    def __init__(
        self, iid: int, question: str, answer: str, deck_id: int, created_at: str
    ) -> None:
        self.iid = str(iid)
        self.question = question
        self.answer = answer
        self.deck_id = deck_id
        self.created_at = created_at

    def get_iid(self):
        return self.iid

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_deck_id(self):
        return self.deck_id
