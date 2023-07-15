
import ctypes
import os
import pkgutil
import sys

dependencies = {
    0: 'keyboard',
    1: 'pyautogui',
    2: 'PyQt5'
}

for i in range(len(dependencies)):
    installCheck = pkgutil.find_loader(dependencies[i])

    if not installCheck:
        try:
            os.system(f"pip3 install {dependencies[i]}")
        except ImportError:
            print(f"pip3 install {dependencies[i]} failed")
    else:
        print(f"found {dependencies[i]} skipping...")
        
from PyQt5.QtWidgets import QApplication, QWidget

# Create a subclass of QWidget
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)  # Set the position and size of the window
        self.setWindowTitle('My Window')  # Set the window title
        self.show()  # Display the window

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of MyWindow
window = MyWindow()

# Start the event loop
sys.exit(app.exec_())

input()