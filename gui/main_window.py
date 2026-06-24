from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

from gui.sidebar import Sidebar
from gui.chat_widget import ChatWidget
from gui.input_widget import InputWidget
from core.assistant_core import handle_input

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Assistant")
        self.resize(1000, 700)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()

        self.sidebar = Sidebar()

        right_layout = QVBoxLayout()

        self.chat = ChatWidget()
        self.input = InputWidget()

        self.input.send_btn.clicked.connect(
            self.send_message
        )

        right_layout.addWidget(self.chat)
        right_layout.addWidget(self.input)

        main_layout.addWidget(self.sidebar)
        main_layout.addLayout(right_layout)

        central.setLayout(main_layout)

    def send_message(self):

        text = self.input.input_box.text()

        if not text:
            return
        
        self.chat.add_message(f"You: {text}")
        response = handle_input(text)
        self.chat.add_message(f"Assistant: {response}")
        self.input.input_box.clear()