#file io
'''
# file = open('filename', 'mode')
f = open('test.txt', 'a')
f.write('first line\n')
f.write('second line\n')
f.close()

f = open('test.txt', 'r')
entireFile = f.read()
print(entireFile + '\n')

f.seek(0)
contents = []
for line in f:
    contents.append(line)

print(contents[0], contents[1])

f.close()
'''
even = [x for x in range(1, 11) if x%2==0]
odd = [x for x in range(1, 11) if x not in even]
evenFile = open('even.txt', 'w')
oddFile = open('odd.txt', 'w')

for i in range(1, 11):
    evenFile.write(str(i) + ' ') if i in even else oddFile.write(str(i) + ' ')

evenFile.close()
oddFile.close()

evenFile = open('even.txt', 'r')
oddFile = open('odd.txt', 'r')

for line in evenFile:
    print(line)
for line in oddFile:
    print(line)

print('even.txt size: {} bytes'.format(evenFile.tell()))
print('odd.txt size: {} bytes'.format(oddFile.tell()))

