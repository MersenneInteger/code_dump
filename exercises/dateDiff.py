#calculate the number of days between two dates
# years months days
import sys

argLength = len(sys.argv)
diffList = ['','','']
if argLength == 7:
    for i in range(1, 4):
        diffList[i-1] = abs(int(sys.argv[i]) - int(sys.argv[i+3]))
    print('Years: {}\nMonths: {}\nDays: {}'.format(diffList[0], diffList[1], diffList[2]))
