from src.controllers.controller import Controller
from src.models.model import Model

from src.views.view import View


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == "__main__":
    main()
