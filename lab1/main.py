from models.directory import Directory
from models.binaryFile import BinaryFile
from models.logTextFile import LogTextFile
from models.bufferFile import BufferFile

#directories
rootDirectory = Directory('root', 42)
directory1 = Directory('directory1', 6, rootDirectory)
directory2 = Directory('directory2', 9, directory1)


#binary files
print('binary files')
binary1 = BinaryFile('binary1', 'some text', rootDirectory)
binary2 = BinaryFile('binary2', 'another text', directory1)
print('binary1 content: ' + binary1.read())
print('binary2 content: ' + binary2.read())
print('----------------\n\n')


#log files
print('log files')
log1 = LogTextFile('log1', directory1)
log1.addLog('log1')
log1.addLog('log3')
log2 = LogTextFile('log2', directory2)
log2.addLog('log2')
print('log1 logs: ' + log1.read())
print('log1 logs: ' + log2.read())
print('----------------\n\n')


#buffer files
print('buffer files')
buffer1 = BufferFile('buffer1', 10, rootDirectory)
buffer1.push('q1')
buffer1.push('q2')
buffer1.push('q3')
buffer2 = BufferFile('buffer2', 20, directory1)
buffer2.move(directory2)
print('buffer1.consume: ' + buffer1.consume())
print('buffer1.consume: ' + buffer1.consume())
print('buffer1.consume: ' + buffer1.consume())
print('----------------\n\n')


print(rootDirectory.listElements())