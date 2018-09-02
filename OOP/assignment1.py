#!usr/bin/python
class MaxSizeList(object):
    
    def __init__(self, maxSize):

        self.maxSize = maxSize
        self.itemList = []
    
    def getMaxSize(self):

        return self.maxSize

    def setMaxSize(self, maxSize):

        self.maxSize = maxSize

    def push(self, item):
        
        if len(self.itemList) == self.maxSize:
            self.itemList.pop(0)
        elif len(self.itemList) > self.maxSize:
            diff = len(self.itemList) - self.maxSize 
            for i in range(diff, -1, -1):
                self.itemList.pop(i)
        self.itemList.append(item)
    
    def getItemList(self):
        
        return self.itemList

aList = MaxSizeList(3)
print('Max Size: {}'.format(aList.getMaxSize()))
aList.push('a')
aList.push('b')
aList.push('c')
aList.push('d')
print(aList.getItemList())
aList.push('e')
print(aList.getItemList())

#change max size
aList.setMaxSize(1)
aList.push('f')
print(aList.getItemList())
aList.setMaxSize(5)
aList.push('g')
aList.push('h')
aList.push('i')
aList.push('j')
aList.push('k')
print(aList.getItemList())
aList.setMaxSize(2)
aList.push('l')
print(aList.getItemList())

#instructor solution
class AltMaxSizeList(object):

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.innerList = []

    def push(self, obj):
        self.innerList.append(obj)
        if len(self.innerList) > self.maxSize:
            self.innerList.pop(0)
    
    def getList(self):
        return self.innerList

