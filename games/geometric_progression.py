'''
basically, made only for the class below
'''

import random

class GeometricProgression:
    '''
    get_numbers returns a list of 5 numbers in geometric progression
    one of the numbers is replaced with zero
    '''
    def __init__(self):
        self.numbers = self._generate_numbers()
        self.replaced_number = self._replace_number()

    def _generate_numbers(self):
        # Generate a random starting number and a common ratio
        start = random.randint(1, 10)
        ratio = random.randint(2, 10)  # Common ratio for the progression
        return [start * (ratio ** i) for i in range(5)]

    def _replace_number(self):
        index_to_replace = random.randint(0, 4)  # Choose an index to replace with zero
        replaced_number = self.numbers[index_to_replace]
        self.numbers[index_to_replace] = 0  # Replace with zero
        return replaced_number

    def get_numbers(self):
        '''Get generated numbers (with one number replaced by zero)'''
        return self.numbers

    def get_answer(self):
        '''Get the replaced number'''
        return self.replaced_number

    def is_correct_answer(self, answer):
        return answer == self.get_answer()
