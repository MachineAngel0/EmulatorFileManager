import os
import sys
import string

# ive left these out so the GUI isn't bloated

optional_emulators = ["Nes", "SNES", "N64", "GameCube", "Wii", "Wii U", "Switch", "Game Boy", "Game Boy Color",
                      "Game Boy Advance", "Sega Saturn", "Sega Dreamcast", "PSP Vita", "PS4", "Xbox", "Xbox 360", ]

# these two should make to each other based on the emulator
emulators_names = ["3DS", "DS", "PS1", "PS2", "PS3", "PSP",]
emulators_exe_name_list = ["citra-qt", "DeSmuME", "duckstation", "pcsx2-qt", "rpcs3", "PPSSPPWindows", ]

emulator_name_to_exe_name = {}
for i in range(len(emulators_names)):
    emulator_name_to_exe_name[emulators_names[i]] = emulators_exe_name_list[i]


# uncomment if i want to add the other emulators
# emulators_names.extend(optional_emulators)

# Output: My name is Alice and I am 30 years old.
# Output: My name is Bob and I work as an engineer.

# gets the roots drives on the system
def get_root_drives():
    # print(os.listdrives())
    return os.listdrives()


# might want to be careful about this
def iterate_through_directory(root_directory='C:\\', file_extention='.exe'):
    found_exe = []

    for root, subdirectories, files in os.walk(root_directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if filepath.lower().endswith(file_extention):
                found_exe.append(filepath)


    # print(found_exe)
    return found_exe


# returns a dict of the emulator name to the emulator file location
def iterate_through_all_directories():
    root_drives = get_root_drives()

    extension_to_parse = []

    for root_directory in root_drives:
        # not using append because it gives us list[list[str]], which is not what we want, we want list[str]
        # extend adds elements to the end of the array
        extension_to_parse.extend(iterate_through_directory(root_directory, '.exe'))

    # print(extension_to_parse)
    # return extension_to_parse
    # parse exe for what im looking for, and then move to its own function when done

    found_emulators = {}
    # hash to store emulator to filepath
    #

    for filepath in extension_to_parse:
        head, tail = os.path.split(filepath)
        # print(head)
        # print(tail)
        # find if emulator is within the list

        # removes .exe from the file name
        tail_without_extension = os.path.splitext(tail)[0]

        # check if the emulator name is within the filename
        '''
        for emulator_name_from_list in emulators_exe_name_list:
            if emulator_name_from_list in tail_without_extension:
                print(f"Found: {tail_without_extension}")
                print(f"Found: {emulator_name_from_list}")
                found_emulators[emulator_name_from_list] = filepath
        '''

        for key, value in emulator_name_to_exe_name.items():
            if value in tail_without_extension:
                print(f"Found: {tail_without_extension}")
                print(f"Found: {value}")
                found_emulators[key] = filepath

    print(found_emulators)
    return found_emulators
    """
    // tests to open up one of the exe's
    test = list(found_emulators.values())
    os.startfile(test[0])
    """
# iterate_through_all_directories()
