from typing import TYPE_CHECKING
from tkinter import END

if TYPE_CHECKING:
    from ..views.main_view import MainView
    from ..models.translator_service import TranslatorService


class AppController:

    def __init__(self, model: "TranslatorService", view: "MainView") -> None:
        self.model = model
        self.view = view
        self.bind_events()

    def bind_events(self) -> None:
        self.view.translate_button.config(command=self.on_translate)

    def on_translate(self) -> None:
        source_text = self.view.input_text.get("1.0", "end-1c").strip()

        translated_text = self.model.translate(source_text)

        self.view.output_text.config(state="normal")
        self.view.output_text.delete("1.0", END)
        self.view.output_text.insert("1.0", translated_text)
        self.view.output_text.config(state="disabled")
