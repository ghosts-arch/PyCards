from src.database import Database
from src.controllers.controller import Controller
from src.models.model import Model

from src.views.view import View


def main():
    database = Database()
    database.connect()
    database.init()
    model = Model(database=database)
    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == "__main__":
    main()
