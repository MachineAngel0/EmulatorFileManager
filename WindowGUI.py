import os
import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, \
    QComboBox
from PyQt6.uic import loadUi
from PyQt6.uic.Compiler.qtproxies import QtCore
from PyQt6 import QtCore, QtGui, QtWidgets

import DirectoryIterator

from OpenExeUtility import open_exe
from JsonUtility import JsonUtilityClass
from FileExtractor import FileExtractor

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)


# (".", "EmulatorFileManager3.ui")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Change the current dir to the temporary one created by PyInstaller

        loadUi("EmulatorFileManager3.ui", self)
        # init the drop box
        self.emulator_drop_box = None
        self.add_emulators_to_drop_down()

        VerticalLayout = self.findChild(QVBoxLayout, "VFileLayout")

        # ref of widgets, to get lookup by emulator name
        self.emulator_row_widgets = {}

        for i in DirectoryIterator.emulators_names:
            widget = Emulator_HorizontalRow()
            widget.generate_layout(i)
            VerticalLayout.addLayout(widget.HLayout)
            self.emulator_row_widgets[i] = widget

        # compressed game file locator
        self.ZipButton = self.findChild(QPushButton, "Label_ZipLocation")
        self.ZipButton.setMaximumSize(QtCore.QSize(256, 32))
        self.ZipButton.clicked.connect(lambda state: self.file_picker_handler(self.ZipButton))

        # when the button is pressed, get the zip button file path, check if its valid,
        # then check the emulator game button file location
        ExtractButton = self.findChild(QPushButton, "Button_Extract")
        ExtractButton.clicked.connect(lambda state: self.ExtractFile_Handler())

        # set up the find emulators button
        FindEmulatorsButton = self.findChild(QPushButton, "Button_FindEmulators")
        FindEmulatorsButton.clicked.connect(lambda state: self.FindEmulators_Handler())

        # handles quitting the application
        QuitButton = self.findChild(QAction, "Quit_Button")
        QuitButton.triggered.connect(lambda state: self.QuitPYQT_Handler())

    def add_emulators_to_drop_down(self):
        self.emulator_drop_box = self.findChild(QComboBox, "EmulatorDropBox")

        self.emulator_drop_box.clear()

        for i in DirectoryIterator.emulators_names:
            self.emulator_drop_box.addItem(i)

    # extract a game zip/iso/etc... to a folder, using the info the user inputs
    def ExtractFile_Handler(self):
        # get emulator name from dropbox
        current_emulator_name = self.emulator_drop_box.currentText()
        print(current_emulator_name)

        # get the widget holding our emulator info, mainly for the games folder directory
        current_widget = self.emulator_row_widgets[current_emulator_name]
        widget_game_folder = current_widget.Button_GameFolder.text()
        print(widget_game_folder)

        # get our zip*(compressed game file) file path
        zip_file_path = self.ZipButton.text()
        print(zip_file_path)

        # zip file, game folder
        FileExtractor(zip_file_path, current_widget.Button_GameFolder.text())

    # duplicate code but whatever for now
    # user picks a file
    def file_picker_handler(self, button_ref):
        dialog = QFileDialog()
        dialog.exec()

        if dialog:
            selectedFiles = dialog.selectedFiles()
            print(selectedFiles)
            # button_ref.update()
            button_ref.setText(selectedFiles[0])
            print(button_ref.text())
        else:
            button_ref.setText("Select Folder")

    # find emulators on the persons device
    def FindEmulators_Handler(self):
        print("pressed")

        emulator_to_file_paths = DirectoryIterator.iterate_through_all_directories()
        for key, value in emulator_to_file_paths.items():
            self.emulator_row_widgets[key].Button_ExeLocation.setText(value)
            # save to file
            JsonUtilityClass().set_new_emulator_path_json(key, JsonUtilityClass().emulator_file_json_name, value)

    def QuitPYQT_Handler(self):
        QApplication.instance().quit()


class Emulator_HorizontalRow(QMainWindow):
    def __init__(self):
        super(Emulator_HorizontalRow, self).__init__()

        loadUi("EmulatorFileManager3.ui", self)
        self.emulator_name = None
        self.HLayout = None
        self.Label_EmulatorName = None
        self.Label_exe = None

        self.Button_ExeLocation = None
        self.Label_GameFolder = None
        self.Button_GameFolder = None
        self.Button_OpenExe = None

        self.JsonUtilityInstance = JsonUtilityClass()

        # the class that creates this must call the generate layout manually
        # self.generate_layout("3DS")

    def generate_layout(self, EmulatorName):
        self.emulator_name = EmulatorName

        # needed for alignment
        _translate = QtCore.QCoreApplication.translate

        # make horizontal layout and set horizontal layout name
        self.HLayout = QHBoxLayout()
        self.HLayout.setObjectName("testLayout")

        self.Label_EmulatorName = QLabel(parent=self.centralwidget)
        self.Label_EmulatorName.setMinimumSize(64, 32)
        self.Label_EmulatorName.setScaledContents(False)
        self.Label_EmulatorName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_EmulatorName.setObjectName("Test_ds")
        self.Label_EmulatorName.setText("Test_ds")
        self.Label_EmulatorName.setText(_translate("MainWindow", EmulatorName))

        self.Label_exe = QLabel(parent=self.centralwidget)
        self.Label_exe.setObjectName("label_16")
        self.Label_exe.setText("Exe Location")

        self.Button_ExeLocation = QPushButton(parent=self.centralwidget)
        self.Button_ExeLocation.setObjectName("ExeLocation_FileDialogue_2")
        self.Button_ExeLocation.setText(
            self.JsonUtilityInstance.query_json_emulator_path(self.emulator_name,
                                                              self.JsonUtilityInstance.emulator_file_json_name))
        self.Button_ExeLocation.setMaximumSize(QtCore.QSize(256, 32))

        # button binding
        self.Button_ExeLocation.clicked.connect(
            lambda state: self.file_picker(self.Button_ExeLocation, self.JsonUtilityInstance.emulator_file_json_name))

        self.Label_GameFolder = QLabel(parent=self.centralwidget)
        self.Label_GameFolder.setObjectName("label_17")
        self.Label_GameFolder.setText("Game Folder:")

        self.Button_GameFolder = QPushButton(parent=self.centralwidget)
        self.Button_GameFolder.setObjectName("pushButton_25")
        self.Button_GameFolder.setText(self.JsonUtilityInstance.query_json_emulator_path(self.emulator_name,
                                                                                         self.JsonUtilityInstance.emulator_game_file_json_name))
        self.Button_GameFolder.setMaximumSize(QtCore.QSize(256, 32))
        # button binding
        self.Button_GameFolder.clicked.connect(lambda state: self.directory_picker(self.Button_GameFolder,
                                                                                   self.JsonUtilityInstance.emulator_game_file_json_name))

        self.Button_OpenExe = QPushButton(parent=self.centralwidget)
        self.Button_OpenExe.setObjectName("pushButton_38")
        self.Button_OpenExe.setText("Launch")
        # bind to open EXE file
        self.Button_OpenExe.clicked.connect(lambda state: self.open_exe_handler(self.Button_ExeLocation.text()))

        # add labels and buttons to the horizontal layout
        self.HLayout.addWidget(self.Label_EmulatorName)
        self.HLayout.addWidget(self.Label_exe)
        self.HLayout.addWidget(self.Button_ExeLocation)
        self.HLayout.addWidget(self.Label_GameFolder)
        self.HLayout.addWidget(self.Button_GameFolder)
        self.HLayout.addWidget(self.Button_OpenExe)

    def find_emulators_handler(self):
        print("insert directory searcher here")

    def file_picker(self, button_ref, json_file_name):
        text_before_change = button_ref.text()
        dialog = QFileDialog()
        dialog.exec()

        selectedFiles = dialog.selectedFiles()
        if selectedFiles:
            print(selectedFiles)
            # button_ref.update()
            button_ref.setText(selectedFiles[0])

            # write to json file
            self.JsonUtilityInstance.set_new_emulator_path_json(self.emulator_name, json_file_name, selectedFiles[0])

            print(button_ref.text())
        else:
            if text_before_change:
                button_ref.setText(text_before_change)
                # write to json file
                #self.JsonUtilityInstance.set_new_emulator_path_json(self.emulator_name, json_file_name,
                                                                    #text_before_change)
            else:
                button_ref.setText("Select A Folder")
                # write to json file
                self.JsonUtilityInstance.set_new_emulator_path_json(self.emulator_name, json_file_name,
                                                                    "Select A Folder")

    def directory_picker(self, button_ref, json_file_name):

        text_before_change = button_ref.text()
        # dialog itself will return the directory path
        dialog = QFileDialog.getExistingDirectory(None, "Select Directory")

        if dialog:
            print(dialog)
            button_ref.update()
            button_ref.setText(dialog)

            # write to json file
            self.JsonUtilityInstance.set_new_emulator_path_json(self.emulator_name, json_file_name, dialog)

            print(button_ref.text())
        else:
            if text_before_change:
                button_ref.setText(text_before_change)
                self.JsonUtilityInstance.set_new_emulator_path_json(self.emulator_name, json_file_name,
                                                                    text_before_change)
            else:
                button_ref.setText("Select A Folder")
                self.JsonUtilityInstance.set_new_emulator_path_json(self.emulator_name, json_file_name,
                                                                    "Select A Folder")

    def open_exe_handler(self, file_path):
        print(file_path)
        open_exe(file_path)
