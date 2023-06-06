import itertools
import sys
import os
from time import sleep

print('Iterator\n')  

DATA = input('Enter characters to iterate all combinations: \n')

# Please consider your processing power
print('Note: Consider character length and storage...\n')

DATA_length = len(DATA)

try:
    with open('Results.txt', 'w+') as f:
        result = itertools.product(DATA, repeat=int(DATA_length))
        for item in result:
            f.write(''.join(item) + '\n')

    sleep(1)

    print('Success! Check \'Results.txt\'.\n')

except Exception as e:
    print('An error occurred:', e)
    sys.exit(1)

