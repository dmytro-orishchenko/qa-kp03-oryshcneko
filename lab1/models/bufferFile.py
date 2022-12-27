class BufferFile:
    def __init__(self, fileName, maxSize = 0, father = None):
        self.MAX_BUF_FILE_SIZE = maxSize
        self.fileName = fileName
        self.father = father
        self.content = []

    def __delete__(self):
        return

    def move(self, path):
        return

    def push(self, elem):
        return

    def consume(self):
        return