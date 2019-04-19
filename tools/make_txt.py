
class MakeTxt:
    def __init__(self):
        self.folder_files = "files/"
        self.extension = ".txt"

    def save_data(self, file, data):
        with open(self.folder_files + file + self.extension, "a") as fc:
            fc.write(data)

    def read_data(self, file):
        file = open(self.folder_files + file + self.extension, "r")
        data = file.read()
        file.close()

        data_list = data.strip().split('\n')

        return data_list
