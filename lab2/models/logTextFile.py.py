class LogTextFile:
    def __init__(self, parent, name, info):
        if (parent.count_elems >= parent.DIR_MAX_ELEMS ):
            print('Parent directory is full.')
            return
        self.parent = parent
        self.name = name
        self.info = info
        self.parent.count_elems += 1
        self.parent.list.append(self)

    def __delete__(self, instance):
        print('Directory was deleted.')
        return

    def move(self, location):
        if (location.count_elems >= location.DIR_MAX_ELEMS):
            print('Directory is full. Can\'t move.')
            return
        self.parent.count_elems -=1 
        index = self.parent.list.index(self)
        self.parent.list.pop(index)
        self.parent = location
        self.parent.list.append(self)
        self.parent.count_elems +=1 
    
    def read(self):
        return self.info

    def append_line(self, line):
        self.info += '\n'
        self.info += line