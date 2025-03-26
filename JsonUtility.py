import os
import json

from DirectoryIterator import emulators_names
from MacroDebug import DEBUG


# 'r' to read, 'w' to write, 'a' to append, 'r+' to read/write

class JsonUtilityClass:
    # the file json_file_name will be one of these two values based on what were doing
    # i could use enums but they look are trash
    emulator_file_json_name = "EmulatorsPaths.json"
    emulator_game_file_json_name = "EmulatorsGamePaths.json"

    def create_json_file(self, current_directory, json_file_name):
        print(f"Current Directory is: {current_directory}")
        emulators_names_to_path = {}

        # init paths for the json file
        for i in range(len(emulators_names)):
            emulators_names_to_path[emulators_names[i]] = "Select A Folder"

        if DEBUG:
            print(emulators_names_to_path)

        file_name = os.path.join(current_directory, json_file_name)

        json_file = open(file_name, 'w')
        # write emulators to path into the file
        json_file.seek(0)
        json.dump(emulators_names_to_path, json_file, indent=4)
        #json_file.write(json.dumps(emulators_names_to_path, ensure_ascii=False, indent=4))
        json_file.close()

        if DEBUG:
            print("Emulator Files Registered to json file")

    def read_file_emulator_test(self, json_file_name):
        file_name = os.path.join(os.getcwd(), json_file_name)
        json_file = open(file_name, 'r')
        data = json.load(json_file)
        print(data)
        print(data["3DS"])
        json_file.close()

    def query_json_emulator_path(self, emulator_name, json_file_name):
        # read from file and get the emulator path

        print("query Json File Entered")
        file_name = os.path.join(os.getcwd(), json_file_name)
        print(file_name)
        if not os.path.exists(file_name):
            print("Querying Json file, file not found, creating it now")
            self.create_json_file(os.getcwd(), json_file_name)



        json_file = open(file_name, 'r')
        # get data from file
        data = json.load(json_file)
        # query for the data
        if self.is_valid_json_index(data, emulator_name):
            print("Querying Json file, valid index")
            file_path = data[emulator_name]
            json_file.close()
            return file_path
        else:
            json_file.close()
            return None

    def is_valid_json_index(self, dict_data, emulator_name) -> bool:
        if emulator_name in dict_data:
            if DEBUG:
                print(True, "|Emulator Was Found In Json File")
            return True
        else:
            if DEBUG:
                print(False, "|Emulator Was Not Found In Json File")
            return False

    def set_new_emulator_path_json(self, emulator_name, json_file_name, file_path):

        # doesn't check to see if path/file exists

        print(json_file_name)

        file_name = os.path.join(os.getcwd(), json_file_name)
        if not os.path.exists(file_name):
            print("Querying Json file, file not found, creating it now")
            self.create_json_file(os.getcwd(), json_file_name)

        # open for reading
        with open(file_name) as f:
            data = json.load(f)
        if DEBUG:
            print(data)
            print(data[emulator_name])
        # set new emulator path
        data[emulator_name] = file_path
        # write to file
        with open(file_name, "w") as f:
            json.dump(data, f)
        # close file
        f.close()


    def unit_test_json_utility(self):
        self.create_json_file(os.getcwd(), self.emulator_file_json_name)
        self.set_new_emulator_path_json("3DS", self.emulator_file_json_name, "D://")
        self.set_new_emulator_path_json("PSP", self.emulator_file_json_name, "D://")
        self.query_json_emulator_path("3DS", self.emulator_file_json_name)
        self.query_json_emulator_path("DS", self.emulator_file_json_name)
        self.query_json_emulator_path("NES", self.emulator_file_json_name)

# JsonUtilityClass().unit_test_json_utility()
