from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton
)


class InputWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.input_box = QLineEdit()

        self.voice_btn = QPushButton("🎤")
        self.send_btn = QPushButton("Send")

        layout.addWidget(self.input_box)
        layout.addWidget(self.voice_btn)
        layout.addWidget(self.send_btn)

        self.setLayout(layout)