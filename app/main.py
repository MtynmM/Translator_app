from .controllers.app_controller import AppController
from .views.main_view import MainView
from .models.translator_service import TranslatorService


class App:
    def __init__(self) -> None:
        self.model = TranslatorService()
        self.view = MainView()

        self.controller = AppController(self.model, self.view)

        self.view.mainloop()


if __name__ == "__main__":
    app = App()
