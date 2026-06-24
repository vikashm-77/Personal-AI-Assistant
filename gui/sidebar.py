from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.chat_btn = QPushButton("Chat")
        self.gesture_btn = QPushButton("Gesture Mode")
        self.memory_btn = QPushButton("Memory")
        self.settings_btn = QPushButton("Settings")

        layout.addWidget(self.chat_btn)
        layout.addWidget(self.gesture_btn)
        layout.addWidget(self.memory_btn)
        layout.addWidget(self.settings_btn)

        layout.addStretch()

        self.setLayout(layout)