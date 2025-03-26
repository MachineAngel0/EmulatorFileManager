import os
import shutil


def is_exe_on_drive(name):
    # finds if the file is executable
    if shutil.which(name):
        return True

    return False


def open_exe(exe_path):
    if is_exe_on_drive(exe_path):
        os.startfile(exe_path)
    else:
        print("cannot open EXE invalid path")

# function for testing
def exe_unit_test():
    file_test_path = "Adobe Substance 3D Painter.exe"
    path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Substance 3D Painter 2024\\Adobe Substance 3D Painter.exe"

    if is_exe_on_drive(file_test_path):
        open_exe(file_test_path)
    else:
        print(f"not a valid path {file_test_path}")

    if is_exe_on_drive(path):
        open_exe(path)
    else:
        print(f"not a valid path {path}")
