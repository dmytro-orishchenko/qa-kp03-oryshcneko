class Directory:
    def __init__(self, dirName, maxElements = 0, father = None):
        self.DIR_MAX_ELEMS = maxElements
        self.father = father
        if self.father != None:
            self.father.elementsCount += 1
            father.fileList.append(self)
        self.name = dirName
        self.elementsCount = 0
        self.fileList = []

    def __delete__(self):
        print(self.dirName + ' directory was deleted')
        return

    def listElements(self, tabulation = ''):
        answ = ''
        for item in self.fileList:
            if type(item) is Directory:
                answ += tabulation + '===>' + self.name + '\n'
                tabulation += '  '
                answ += item.listElements(tabulation + '  ')
                answ += tabulation + '<===\n'

            else:
                answ += tabulation + item.fileName + ', ' +'\n' 

        return answ

    def move(self, path):
        if (path.elementsCount >= path.DIR_MAX_ELEMS + 1):
            print('Target directory is full')
            return

        if self.father != None:
            self.father.elementsCount -= 1
            self.father.fileList.pop(self.father.fileList.index(self))

        self.father = path
        self.father.fileList.append(self)
        self.father.elementsCount += 1 
        return