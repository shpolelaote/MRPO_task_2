'''does some shit'''
import sys
import os

# Get the parent directory path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)

# Now you can import your script
import cli  # Replace with the actual script name (without the .py)
import games.geometric_progression as gm
import games.lcm as lcm

cli.welcome_to_brain_games()

while True:
    print('Choose the game: LCM (least common multiple) or GM (geometric progression).')
    choice = input().strip().upper()
    if choice not in ['LCM', 'GM']:
        print('Incorrect input! Write LCM or GM.')
        continue
    current_game = gm.GeometricProgression()

    for i in range(3):
        if choice == 'GM':
            current_game = gm.GeometricProgression()
        elif choice == 'LCM':
            current_game = lcm.LeastCommonMultiple()
        print(f'Round {i}.')

        print(', '.join(['...' if x == 0 else str(x) for x in current_game.get_numbers()]))
        given_answer = ''
        while not given_answer.isnumeric():
            given_answer = input('Your answer: ')
            if not given_answer.isnumeric():
                print('Incorrect input. Write an integer.')
        if current_game.is_correct_answer(int(given_answer)):
            print('Correct!')
        else:
            print(f'{given_answer} is wrong answer ;(. \
            Correct answer was{current_game.get_answer()}')
            break
        if i == 2:
            print(f'Congratulations, {cli.name}!')
