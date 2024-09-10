import winreg
import os

def delete_HKEY_CLASSES_ROOT():
    try:
        key_path = r"Directory\\background\\shell\\Samples"
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path, 0, winreg.KEY_WRITE) as key:
            winreg.DeleteKey(key, "")

        print('Раздел реестра успешно удален из "HKEY_CLASSES_ROOT/Directory/background/shell/Samples"')

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def delete_HKEY_LOCAL_MACHINE():
    try:
        command_key_path = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommandStore\\shell\\Sample\\command"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, command_key_path, 0, winreg.KEY_WRITE) as key:
            winreg.DeleteKey(key, "")
            
        shell_key_path = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommandStore\\shell\\Sample"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, shell_key_path, 0, winreg.KEY_WRITE) as key:
            winreg.DeleteKey(key, "")

        print('Разделы реестра успешно удалены из "HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows/CurrentVersion/Explorer/CommandStore/shell"')

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    delete_HKEY_CLASSES_ROOT()
    delete_HKEY_LOCAL_MACHINE()
