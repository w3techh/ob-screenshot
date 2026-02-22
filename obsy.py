#!/usr/bin/env python3

import sys
import subprocess
import datetime
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt  # Add this import

class ScreenshotTool(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Screenshot Tool")
        self.setGeometry(100, 100, 300, 150)
        self.setFixedSize(300, 150)

        # UI components
        self.label = QLabel("Click the button to take a screenshot", self)
        self.label.setAlignment(Qt.AlignCenter)  # Now Qt.AlignCenter is defined

        self.btn_take_screenshot = QPushButton("Take Screenshot", self)
        self.btn_take_screenshot.clicked.connect(self.take_screenshot)

        self.btn_quit = QPushButton("Quit", self)
        self.btn_quit.clicked.connect(self.close)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_take_screenshot)
        layout.addWidget(self.btn_quit)

        self.setLayout(layout)

    def take_screenshot(self):
        try:
            # Create ~/screenshots directory if it doesn't exist
            screenshots_dir = os.path.expanduser("~/Screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Create filename with timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(screenshots_dir, f"screenshot_{timestamp}.png")

            # Minimize window before screenshot
            self.showMinimized()

            # Run scrot with selection mode
            subprocess.run(["scrot", "-s", filename])

            # Restore window
            self.showNormal()

            # Success message
            # QMessageBox.information(self, "Success", f"Screenshot saved as:\n{filename}")

        except Exception as e:
            # Error message
            QMessageBox.critical(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScreenshotTool()
    window.show()
    sys.exit(app.exec_())