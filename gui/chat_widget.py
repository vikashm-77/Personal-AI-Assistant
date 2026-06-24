from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from gui.styles import CHAT_STYLE


class ChatWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setStyleSheet(CHAT_STYLE)

        layout.addWidget(self.chat_area)
        self.setLayout(layout)

    def add_message(self, text, sender="assistant"):

        if sender == "user":
            html = f"""
        <table width="100%" style="margin: 8px 0;">
            <tr>
                <td align="right">
                    <span style="
                        background-color: #10a37f;
                        color: white;
                        padding: 10px 14px;
                        border-radius: 12px;
                        display: inline-block;
                    ">
                        {text}
                    </span>
                </td>
            </tr>
        </table>
        """
        else:
            html = f"""
        <table width="100%" style="margin: 8px 0;">
            <tr>
                <td align="left">
                    <span style="
                        background-color: #2f2f2f;
                        color: white;
                        padding: 10px 14px;
                        border-radius: 12px;
                        display: inline-block;
                    ">
                        {text}
                    </span>
                </td>
            </tr>
        </table>
        """

        self.chat_area.append(html)

        scrollbar = self.chat_area.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())