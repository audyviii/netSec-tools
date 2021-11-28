import itertools
import time

print('Iterator \n')

DATA = input('Type letters, numbers, symbols for iteration. \n')
DATA_len = len(DATA)

with open('Results.txt', 'w+') as quickie:
    result = itertools.product(DATA, repeat=int(DATA_len))
    for item in result:
        #print(''.join(item))
        quickie.write(''.join(item) + '\n')

time.sleep(2)

print('Finished! Check directory for \'Result.txt\'. \n')
