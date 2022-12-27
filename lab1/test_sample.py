from array import array
from models.directory import Directory
from models.binaryFile import BinaryFile
from models.logTextFile import LogTextFile
from models.bufferFile import BufferFile
from types import NoneType

class TestDirectory:
    fatherDirectory = Directory('fatherDir')

    def test_directoryCreation():
        maxElements = 10
        name = 'name1'
        directory = Directory(name, maxElements)

        assert directory.name == name
        assert directory.DIR_MAX_ELEMS == maxElements
        assert directory.elementsCount == 0
        assert type(directory.father) is NoneType
        assert type(directory.listElements()) is list

    def test_directoryMove(self):
        directory = Directory('dir')
        assert type(directory.father) is NoneType

        directory.move(self.fatherDirectory)
        
        assert directory.father == self.fatherDirectory

    def test_directoryDeletion(self):
        directory = Directory('dir')

        del directory

        assert 'directory' not in locals()

class TestBinary:
    fatherDirectory = Directory('fatherDir')

    def test_binaryCreation(self):
        name = 'name1'
        content = 'some file content blah blah blah'
        binary = BinaryFile(name, content, self.fatherDirectory)

        assert binary.name == name
        assert binary.content == content
        assert binary.read() == content
        assert binary.fatherDirectory == self.fatherDirectory

    def test_binaryMove(self):
        name = 'name1'
        content = 'some file content blah blah blah'
        binary = BinaryFile(name, content)
        assert type(binary.father) is NoneType

        binary.move(self.fatherDirectory)
        
        assert binary.father == self.fatherDirectory

    def test_binaryDeletion(self):
        binary = BinaryFile('bin')

        del binary

        assert 'binary' not in locals()

class TestBuffer:
    fatherDirectory = Directory('fatherDir')

    def test_bufferCreation(self):
        name = 'name1'
        size = 10
        buffer = BufferFile(name, size, self.fatherDirectory)

        assert buffer.name == name
        assert buffer.MAX_BUF_FILE_SIZE == size
        assert buffer.consume() is NoneType
        assert buffer.fatherDirectory == self.fatherDirectory

    def test_bufferMove(self):
        name = 'name1'
        content = 'some file content blah blah blah'
        buffer = BufferFile(name, content)
        assert type(buffer.father) is NoneType

        buffer.move(self.fatherDirectory)
        
        assert buffer.father == self.fatherDirectory

    def test_bufferDeletion(self):
        buffer = BufferFile('buffer')

        del buffer

        assert 'buffer' not in locals()

    def test_bufferAddConsume(self):
        name = 'name1'
        size = 10
        line1 = 'line1'
        line2 = 'line2'
        buffer = BufferFile(name, size)
        
        buffer.push(line1)
        buffer.push(line2)


        assert buffer.consume() == line1
        assert buffer.consume() == line2
        assert buffer.consume() is NoneType

class TestLog:
    fatherDirectory = Directory('fatherDir')

    def test_logCreation(self):
        name = 'name1'
        log = LogTextFile(name, self.fatherDirectory)

        assert log.name == name
        assert log.read() is NoneType
        assert log.fatherDirectory == self.fatherDirectory

    def test_logMove(self):
        name = 'name1'
        log = LogTextFile(name)
        assert type(log.father) is NoneType

        log.move(self.fatherDirectory)

        assert log.father == self.fatherDirectory

    def test_logDeletion(self):
        log = LogTextFile('log')

        del log

        assert 'log' not in locals()

    def test_logAddRead(self):
        name = 'name1'
        line1 = 'line1'
        line2 = 'line2'
        log = LogTextFile(name)

        log.addLog(line1)
        log.addLog(line2)


        assert log.read() == line1 + '\n' + line2
