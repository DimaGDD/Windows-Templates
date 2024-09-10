import winreg
import os
import sys
import subprocess

from plyer import notification

script_dir = os.path.dirname(os.path.abspath(__file__))

def HKEY_CLASSES_ROOT():
    try:
        key_path = r"Directory\\background\\shell\\Samples"

        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path) as key:
            winreg.SetValueEx(key, "icon", 0, winreg.REG_SZ, f"{script_dir}\\icon_for_group.ico")
            winreg.SetValueEx(key, "Position", 0, winreg.REG_SZ, "top")
            winreg.SetValueEx(key, "SubCommands", 0, winreg.REG_SZ, "Sample")
            winreg.SetValueEx(key, "MUIVerb", 0, winreg.REG_SZ, "")
        
        print('Раздел реестра и значения успешно созданы в "HKEY_CLASSES_ROOT/Directory/background/shell"')

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def HKEY_LOCAL_MACHINE():
    try:
        key_path = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommandStore\\shell\\Sample"
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            winreg.SetValueEx(key, "icon", 0, winreg.REG_SZ, f"{script_dir}\\icon_for_sample.ico")

        key_path = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommandStore\\shell\\Sample\\command"
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, f"{script_dir}\\main.exe")

        print('Раздел реестра и значения успешно созданы в "HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows/CurrentVersion/Explorer/CommandStore/shell"')
        # a = input()

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    HKEY_CLASSES_ROOT()
    HKEY_LOCAL_MACHINE()