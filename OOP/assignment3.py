#!/usr/bin/python
import sys, os

class ConfigDict(dict):

    def __init__(self, file_name):
        
        self._file_name = file_name
        if os.path.isfile(self._file_name):
            file_handle = open(self._file_name, 'r')
            for line in file_handle:
                line = line.rstrip()
                key, value = line.split('=')
                print(key, value)
                dict.__setitem__(self, key, value)
            file_handle.close()

    def __setitem__(self, key, value):
        
        dict.__setitem__(self, key, value) 
        file_handle = open(self._file_name, 'w')
        for key, val in self.items():
            file_handle.write('{0}={1}\n'.format(key, val))
        file_handle.close()

cd = ConfigDict('config.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    val = sys.argv[2]
    print('writing data to config.txt: {0}, {1}'.format(key, val))
    cd[key] = val
else:
    print('reading data from config.txt')
    for key in cd.keys():
        print('{0}={1}'.format(key, cd[key]))
