
'''
TODO:
- Setup
    - Simulate keyboard inputs to game
    - Get state data from game
    - Determine rewards
    - Create macros for actions
- NN Training
    - Save model
'''

import pyautogui as keyboard
import time
import csv

file_name = 'KyMoveList.csv'

def main():

    init()

    button_map = { 
        '1':('a', 's'),
        '2':('s',),
        '3':('s', 'd'),
        '4':('a',),
        '5':('',),
        '6':('d',),
        '7':('a', 'w'),
        '8':('w',),
        '9':('w', 'd'),
        'p':('u',),
        'k':('j',),
        's':('i',),
        'h':('k',),
        'd':('o',),
        }

    move = '214s'

    down_keys = []
    for input in move:
        key_inputs = button_map[input]
        for key in key_inputs:
            keyboard.keyDown(key)
            if key not in down_keys:
                down_keys.append(key)

        # if input not in 'pkshd': # ['p', 'k', 's', 'h', 'd']
        for down_key in down_keys:
            print(key_inputs)
            print(down_keys)
            if down_key not in key_inputs:
                keyboard.keyUp(key)
                down_keys.remove(key)

        # print(f'After key remove: {down_keys}')

    for down_key in down_keys:
        keyboard.keyUp(down_key)        

    # down_keys = []
    # for key, key_action in move:
    #     if key_action == 1:
    #         keyboard.keyDown(key)
    #         down_keys.append(key)
    #     elif key_action == 0:
    #         keyboard.keyUp(key)
    #         down_keys.remove(key)

    # for down_key in down_keys:
    #     keyboard.keyUp(down_key)

def init():
    print('Starting program...')

    time.sleep(3)

    # keyboard.PAUSE = 0.02

    

def read_csv():
    move_data = {}
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row

        move_inputs = []
        for row in reader:
            move_name = row[0]



if __name__ == '__main__':
    main()

