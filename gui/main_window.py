from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

from voice.tts import speak
from gui.voice_worker import VoiceWorker
from vision.gesture_mode import gesture_mode

from gui.sidebar import Sidebar
from gui.chat_widget import ChatWidget
from gui.input_widget import InputWidget
from core.assistant_core import handle_input

from gui.styles import WINDOW_STYLE


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.voice_worker = None
        

        self.setStyleSheet(WINDOW_STYLE)
        self.setWindowTitle("AI Assistant")
        self.resize(1000, 700)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.sidebar = Sidebar()

        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(16, 16, 16, 16)
        right_layout.setSpacing(12)

        self.chat = ChatWidget()
        self.input = InputWidget()

        self.input.send_btn.clicked.connect(self.send_message)
        self.input.input_box.returnPressed.connect(self.send_message)
        self.input.voice_btn.clicked.connect(self.start_voice_input)
        self.sidebar.gesture_btn.clicked.connect(self.start_gesture_mode)

        right_layout.addWidget(self.chat)
        right_layout.addWidget(self.input)

        right_panel.setLayout(right_layout)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(right_panel)

        central.setLayout(main_layout)

    def send_message(self):
        text = self.input.input_box.text().strip()

        if not text:
            return

        self.input.input_box.clear()
        self.process_user_message(text)

    def start_voice_input(self):
        self.voice_worker = VoiceWorker()
        self.voice_worker.finished.connect(self.handle_voice_result)
        self.voice_worker.start()

    def handle_voice_result(self, text):
        self.process_user_message(text)
        
    def process_user_message(self, text):
        self.chat.add_message(text, sender="user")

        response = handle_input(text)

        if not response:
            response = "I couldn't process that."

        self.chat.add_message(response, sender="assistant")
        speak(response)

        clean_text = text.lower().strip().replace(".", "").replace("!", "").replace(",", "")

        if clean_text in {"exit", "quit", "close assistant", "shutdown assistant"}:
            self.close()
    def start_gesture_mode(self):
        self.chat.add_message("Gesture mode started.", sender="assistant")
        speak("Gesture mode started")

        result = gesture_mode()

        self.chat.add_message("Gesture mode ended.", sender="assistant")
        speak("Gesture mode ended")

    