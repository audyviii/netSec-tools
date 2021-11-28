import os
import time
import sys

print('Welcome... This program is an iteration/comination tool based on user input')
time.sleep(.5)
print('Please type new file name... ')
filename = input('-> ')

try:
    os.makedirs('C0MB0') 
except FileExistsError:
    print('You already have a file with this name. The previous data will be overwritten-- for now. ')
    time.sleep(1.5)

print('\n')
os.chdir('C0MB0')
print('Enter adjective... (case-sensitive)')
adj = input()
print('Enter noun... (case-sensitive)')
noun = input()
time.sleep(1.25)
text = (adj + noun)

#print('Creating a file... What would you like to name it?')
#filename = input()


# number iterations w/ concatenation
f= open("{}.txt".format(filename),"w+")
x = 0
while x < 10:
    f.write(text + str(0) + str(0) + str(x) + '\n')
    x = x + 1

x = 10
while x < 100:
    f.write(text + str(00) + str(x) + '\n')
    x = x + 1

x = 100
while x < 1000:
    f.write(text + str(x) + '\n')
    x = x + 1
f.close()

f= open("readme.txt","w+")
f.write('''This is a README. This is a test.
''')
f.close()
time.sleep(1.5)
print('Success! Please check C0MB0')
