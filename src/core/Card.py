class Card:
    def __init__(
        self, iid: int, question: str, answer: str, created_at, updated_at
    ) -> None:
        self.iid = iid
        self.question = question
        self.answer = answer
        self.created_at = created_at
        self.updated_at = updated_at

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_iid(self):
        return self.iid

    def to(self):
        pass

    @classmethod
    def from_shema(cls, schema):
        return Card(
            iid=schema.id,
            answer=schema.answer,
            question=schema.question,
            created_at=schema.created_at,
            updated_at=schema.created_at,
        )
