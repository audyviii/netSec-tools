import os
import time

def create_folder(folder_name):
    ''' Create a new folder with the specified name '''
    try:
        os.makedirs(folder_name)
    except FileExistsError:
        print('The folder already exists. Please try again with a different name.\n')
        return False
    return True

def intro_inputs():
    ''' Collect folder and file input variables '''
    print('Welcome... This program is an input-based iterator tool.\n')
    time.sleep(0.5)

    folder_name = input('Please enter a new folder name: ')
    while not create_folder(folder_name):
        folder_name = input('Please enter a new folder name: ')

    file_name = input('Please enter a new file name: ')
    return folder_name, file_name

def input_words():
    ''' Collect two words to be iterated '''
    adj = input('Enter the first word (case-sensitive): ')
    noun = input('Enter the noun (case-sensitive): ')
    time.sleep(0.5)
    return adj, noun

def generate_and_write_data(file_name, text, flipped_text):
    ''' Generate and write data to the file '''
    with open('{}.txt'.format(file_name), 'w+') as f:
        numbers = [f'{i:03}' for i in range(1000)]
        for num in numbers:
            f.write(f'{text}' + num + '\n')
            f.write(f'{flipped_text}' + num + '\n')

folder_name, file_name = intro_inputs()
adj, noun = input_words()

text = adj + noun
flipped_text = noun + adj

os.chdir(folder_name) # Move to the created directory

generate_and_write_data(file_name, text, flipped_text)

print('Success!')
