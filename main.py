import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; padding: 10px;")

        # Layouts
        main_layout = QVBoxLayout()
        grid = QGridLayout()

        # Buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        positions = [(i, j) for i in range(4) for j in range(4)]

        for position, text in zip(positions, buttons):
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px;")
            button.clicked.connect(self.on_click)
            grid.addWidget(button, *position)

        main_layout.addWidget(self.display)
        main_layout.addLayout(grid)

        self.setLayout(main_layout)

    def on_click(self):
        button = self.sender()
        text = button.text()

        if text == "C":
            self.display.clear()

        elif text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")

        else:
            self.display.setText(self.display.text() + text)


app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())
