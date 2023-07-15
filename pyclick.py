
import ctypes
import os
import sys
import pkgutil

modules = {
    0: 'keyboard',
    1: 'pyautogui',
    2: 'PyQt5'
    }

for i in range(len(modules)):
    installCheck = pkgutil.find_loader(modules[i])

    if not installCheck:
        try:
            os.system(f"pip3 install {modules[i]}")
        except ImportError:
            print(f"pip3 install {modules[i]} failed")
    else:
        print(f"found {modules[i]} ")

input()