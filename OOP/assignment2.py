#!/usr/bin/python

import datetime, abc

class WriteFile(object):
    
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self, message):
        return

class LogFile(WriteFile):
    
    def __init__(self, filename):
        super(LogFile, self).__init__(filename)
    
    def write(self, message):
        self.f = open(self.filename, 'a')
        dateStr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        message = dateStr + '\t' + message
        self.f.write(message + '\n')
        print(message)
        self.f.close()

class DelimFile(WriteFile):
    
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, itemList):
        self.f = open(self.filename, 'a')
        self.f.write(self.delim.join(itemList))
        print(self.delim.join(itemList))
        self.f.write('\n')
        self.f.close()

log = LogFile('log.txt')
csv = DelimFile('text.csv', ',')

log.write('this is a log message')
log.write('here is another log message')

csv.write(['a', 'b', 'c', 'd'])
csv.write(['1', '2', '3', '4'])
