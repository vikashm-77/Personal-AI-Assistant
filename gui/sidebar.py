from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from gui.styles import SIDEBAR_STYLE


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)
        self.setStyleSheet(SIDEBAR_STYLE)

        layout = QVBoxLayout()
        layout.setContentsMargins(12, 20, 12, 20)
        layout.setSpacing(12)

        self.title = QLabel("AI Assistant")
        self.title.setStyleSheet("color: white; font-size: 18px; font-weight: bold; padding: 6px;")

        self.chat_btn = QPushButton("Chat")
        self.gesture_btn = QPushButton("Gesture Mode")
        self.memory_btn = QPushButton("Memory")
        self.settings_btn = QPushButton("Settings")

        layout.addWidget(self.title)
        layout.addSpacing(10)
        layout.addWidget(self.chat_btn)
        layout.addWidget(self.gesture_btn)
        layout.addWidget(self.memory_btn)
        layout.addWidget(self.settings_btn)

        layout.addStretch()

        self.setLayout(layout)