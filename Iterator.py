import itertools
from time import sleep

print('Iterator \n') # title

DATA = input('Enter characters to iterate all combinations... \n')
print('Note: Consider character length and storage... \n')
DATA_length = len(DATA) 

with open('Results.txt', 'w+') as f:
    result = itertools.product(DATA, repeat=int(DATA_length))
    for item in result:
        f.write(''.join(item) + '\n')

sleep(1)

print('Success! Check \'Iterations-Results.txt\'. \n')
