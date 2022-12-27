class BinaryFile:
    def __init__(self, fileName, content = None, father = None):
        self.file_name = fileName
        self.content = content
        self.father = father

    def __delete__(self):
        return

    def move(self, path):
        return

    def read(self):
        return