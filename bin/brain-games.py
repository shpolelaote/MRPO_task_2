'''does some shit'''
import sys
import os

# Get the parent directory path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

# Now you can import your script
import cli  # Replace with the actual script name (without the .py)
cli.welcome_to_brain_games()

import games.geometric_progression as gm
import games.lcm as lcm

while True:
    print('Choose the game: LCM (least common multiple) or GM (geometric progression).')
    choice = input().strip().upper()
    if choice not in ['LCM', 'GM']:
        print('Incorrect input! Write LCM or GM.')
        continue
    game = None
    
    for i in range(3):
        if choice == 'GM':
            game = gm.GeometricProgression()
        elif choice == 'LCM':
            game = lcm.LeastCommonMultiple()
        print(f'Round {i}.')

        print(', '.join(['...' if x == 0 else str(x) for x in game.get_numbers()]))
        answer = ''
        while not answer.isnumeric():
            answer = input('Your answer: ')
            if not answer.isnumeric():
                print('Incorrect input. Write an integer.')
        if game.is_correct_answer(int(answer)):
            print(f'Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was{game.get_answer()}')
            break
        if i == 2:
            print(f'Congratulations, {cli.name}!')