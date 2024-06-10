
'''
TODO:
- Setup
    - Simulate keyboard inputs to game
        - Handle input flipping for side switch
    - Get state data from game
    - Determine rewards
    - Create macros for actions
- NN Training
    - Save model
'''

from input_handler import InputHandler
import time
import csv


def main():
    init()
    ih = InputHandler()
    move_list = read_csv('KyMoveList.csv')

    ih.do_move(move_list[16][0])
            

def init():
    print('Starting program...')

    time.sleep(3) # Give time to focus window on game

# read csv and return its rows as a list
def read_csv(file_name):

    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        parsed_file = []
        next(reader)
        for row in reader:
            parsed_file.append(row)

        return parsed_file



if __name__ == '__main__':
    main()

