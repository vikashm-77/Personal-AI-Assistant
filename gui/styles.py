# gui/styles.py

WINDOW_STYLE = """
QMainWindow {
    background-color: #1e1e1e;
}
"""

SIDEBAR_STYLE = """
QWidget {
    background-color: #171717;
}

QPushButton {
    background-color: #2a2a2a;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-size: 14px;
    text-align: left;
}

QPushButton:hover {
    background-color: #3a3a3a;
}
"""

CHAT_STYLE = """
QTextEdit {
    background-color: #212121;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-size: 14px;
}
"""

INPUT_STYLE = """
QLineEdit {
    background-color: #2b2b2b;
    color: white;
    border: 1px solid #444;
    border-radius: 10px;
    padding: 10px;
    font-size: 14px;
}

QLineEdit:focus {
    border: 1px solid #666;
}
"""

BUTTON_STYLE = """
QPushButton {
    background-color: #2f2f2f;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 14px;
    font-size: 14px;
}

QPushButton:hover {
    background-color: #3d3d3d;
}
"""

SEND_BUTTON_STYLE = """
QPushButton {
    background-color: #10a37f;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 16px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #0d8c6d;
}
"""