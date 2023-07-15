
import ctypes
import os
import pkgutil

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

from PyQt5.QtWidgets import QApplication, QLabel
app = QApplication([])
label = QLabel('Hello World!')
label.show()

input()