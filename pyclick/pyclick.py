
import ctypes
import os
import sys
import pkgutil

modules = {
    0: 'keyboard',
    1: 'pyautogui',
    2: 'pyqt5'
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
        
'''has_keyboard_installed = pkgutil.find_loader("keyboard") is not None
 
os.system("@echo off")
 
if not has_keyboard_installed:
    try:
        os.system("pip3 install keyboard")
        os.system("cls")
    except ImportError:
        print("pip3 install keyboard failed.")
else:
    print("found")'''


input()