'''meets the player'''
name = None
def welcome_to_brain_games():
    '''meets the player'''
    global name
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
