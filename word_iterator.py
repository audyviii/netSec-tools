import os
import time
import sys

def intro_inputs():
    ''' This function is used to collect folder and file input variables '''

    global file_name, folder_name 
    print('Welcome... This program is an input-based iterator tool. \n')
    time.sleep(.5)

    # Naming the folder/directory that we will store a file within
    folder_name = input('Please type new folder name...  ')

    # Error checking for existing
    try:
        os.makedirs(f'{folder_name}')
    except FileExistsError:
        time.sleep(.5) 
        print('The one you entered already exists... Please try again. \n')
        time.sleep(.5)
        return intro_inputs() 

    file_name = input('Please type new file name...   ')
    move_dir = os.chdir(folder_name) # moving directory to created directory 

def input_words():
    ''' A small function that is focused on recieving two words in both order to be iterated with '''
    
    global text, flipped_text
    adj = input('Enter first word... (case-sensitive) ')
    noun = input('Enter noun... (case-sensitive) ')
    time.sleep(.5)
    text = (adj + noun)
    flipped_text = (noun + adj)  

   
intro_inputs() 
input_words()

with open('{}.txt'.format(file_name),'w+') as f:
    numbers = [f'{i:03}' for i in range(1000)]
    for num in numbers:
        f.write(f'{text}' + num + '\n')
        f.write(f'{flipped_text}' + num + '\n')

print('Success!')
