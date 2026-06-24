from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton
)

from gui.styles import INPUT_STYLE, BUTTON_STYLE, SEND_BUTTON_STYLE


class InputWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type a message...")
        self.input_box.setStyleSheet(INPUT_STYLE)

        self.voice_btn = QPushButton("🎤")
        self.voice_btn.setFixedWidth(50)
        self.voice_btn.setStyleSheet(BUTTON_STYLE)

        self.send_btn = QPushButton("Send")
        self.send_btn.setFixedWidth(90)
        self.send_btn.setStyleSheet(SEND_BUTTON_STYLE)

        layout.addWidget(self.input_box)
        layout.addWidget(self.voice_btn)
        layout.addWidget(self.send_btn)

        self.setLayout(layout)