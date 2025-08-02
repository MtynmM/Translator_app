import ttkbootstrap as ttk
from tkinter import Text, END


class MainView(ttk.Window):

    def __init__(self) -> None:
        super().__init__(themename="darkly")
        self.title("مترجم آنلاین(MTMO)")
        self.geometry("900x650")
        self.resizable(False, False)

        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill="both", expand=True)

        left_frame = ttk.Frame(text_frame)
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = ttk.Frame(text_frame)
        right_frame.pack(side="right", fill="both", expand=True)

        self.input_label = ttk.Label(
            left_frame, text="متن ورودی (Source Text)", font=("Arial", 12)
        )
        self.input_label.pack(pady=7)

        self.input_text = Text(left_frame, height=20, width=40, font=("Arial", 12))
        self.input_text.pack(fill="both", expand=True)

        self.output_label = ttk.Label(
            right_frame, text="متن خروجی (Translated Text)", font=("Arial", 12)
        )
        self.output_label.pack(pady=7)

        self.output_text = Text(
            right_frame, height=20, width=40, font=("Arial", 12), state="disabled"
        )
        self.output_text.pack(fill="both", expand=True)

        self.translate_button = ttk.Button(main_frame, text="ترجمه متن")
        self.translate_button.pack(pady=(15, 0))
