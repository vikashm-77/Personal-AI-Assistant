from PyQt6.QtCore import QThread, pyqtSignal
from voice.speech import recognize


class VoiceWorker(QThread):
    finished = pyqtSignal(str)

    def run(self):
        text = recognize()

        if text:
            self.finished.emit(text)