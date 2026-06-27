from PyQt6.QtCore import QThread, pyqtSignal
from vision.gesture_mode import gesture_mode


class GestureWorker(QThread):
    finished = pyqtSignal(str)

    def run(self):
        result = gesture_mode()

        if not result:
            result = "EXIT"

        self.finished.emit(result)