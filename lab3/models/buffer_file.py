from itertools import count


class BufferFile:
    def __init__(self, parent, max_size, name):
        if (parent.count_elems >= parent.DIR_MAX_ELEMS ):
            print('Parent directory is full')
            return
        self.parent = parent
        self.parent.count_elems += 1
        self.parent.list.append(self)
        self.MAX_BUF_FILE_SIZE = max_size
        self.name = name
        self.info = []

    def __delete__(self, instance):
        print('Directory was deleted.')
        return

    def move(self, location):
        if (location.count_elems >= location.DIR_MAX_ELEMS):
            return
        self.parent.count_elems -=1 
        index = self.parent.list.index(self)
        self.parent.list.pop(index)
        self.parent = location
        self.parent.list.append(self)
        self.parent.count_elems +=1 
    
    def push(self, elem):
        if len(self.info) >= int(self.MAX_BUF_FILE_SIZE):
            print('File is full. Can\'t push new line.')
            return
        self.info.append(elem)

    def consume(self):
        self.info.pop()