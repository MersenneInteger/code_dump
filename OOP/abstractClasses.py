#!usr/bin/python
import abc

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, val):
        self.val = 0
    def setVal(self, val):
        self.val = val
    def getVal(self):
        return self.val
    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):
    def setVal(self, val):
        if not isinstance(val, int):
            val = 0
        super(GetSetInt, self).setVal(val)
    def showdoc(self):
        print('GetSetInt object ({}) only accepts integer values'.format(id(self)))

class GetSetList(GetSetParent):
    def __init__(self, val=0):
        self.valList = [val]
    def getVal(self):
        return self.valList[-1]
    def getVals(self):
        return self.valList
    def setVal(self, val):
        self.valList.append(val)
    def showdoc(self):
        print('GetSetList object ({0}), len {1} stores values'.format(id(self), len(self.valList)))

#intObj.val will equal 0 bc it doesnt overload the parents __init__
intObj = GetSetInt(2)
#listObj.val will equal 3 bc it does overload the parents __init__
listObj = GetSetList(3)
listObj.setVal(5)
print(intObj.getVal())
print(listObj.getVals())
