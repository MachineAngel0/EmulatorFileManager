import os
import shutil

import patoolib


def FileExtractor(FilePath, ExtractPath):
    # zip file, path to send to

    FilePathName = os.path.basename(os.path.normpath(FilePath))
    print(FilePathName)

    # remove the .file_ext
    print(f"Game File: {FilePathName} ")
    head, tail = os.path.splitext(FilePathName)
    print("Head", head, "Tail", tail)

    ExtractPath_Dir = ExtractPath + "/" + head
    print(ExtractPath_Dir)

    # patoolib.extract_archive(FilePath, outdir= ExtractPath + f"/{head}")
    patoolib.extract_archive(FilePath, outdir=ExtractPath_Dir)

    # move the compressed file to the new folder
    shutil.move(FilePath, ExtractPath_Dir)


# test files, everything works perfectly

temp_7z_file_path = "C:\\Users\\Adams Humbert\\Downloads\\TF3\\Yu-Gi-Oh! Duel Monsters GX Tag Force 3 (English 07-29-21).7z"
temp_7z_extract_file_path = "C:\\Users\\Adams Humbert\\Downloads\\TF3"
temp_rar_file_path = "C:\\Users\\Adams Humbert\\Downloads\\WC2011\\5720 - Yu-Gi-Oh! 5D's World Championship 2011 - Over the Nexus (U).rar"
temp_rar_extract_file_path = "C:\\Users\\Adams Humbert\\Downloads\\WC2011"

# FileExtractor(temp_rar_file_path, temp_rar_extract_file_path)
# FileExtractor(temp_7z_file_path, temp_7z_extract_file_path)
