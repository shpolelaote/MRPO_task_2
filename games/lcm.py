'''
module for least common multiple game
has relative class
'''
import random
import math

class LeastCommonMultiple:
    '''
    get_numbers returns a list of 3 numbers that do not exceed 100
    the numbers' least common multiple do not exceed 100
    '''
    def __init__(self):
        self.numbers = self._generate_numbers()
        self.lcm = self._find_lcm()

    def _generate_numbers(self):
        numbers = []
        while True:
            numbers = [random.randint(1, 100) for _ in range(3)]
            if self._find_lcm(*numbers) <= 100:
                break
        return numbers

    def _find_lcm(self, a=None, b=None, c=None):
        if a is None or b is None or c is None:
            a, b, c = self.numbers
        lcm_ab = abs(a * b) // math.gcd(a, b)
        lcm_abc = abs(lcm_ab * c) // math.gcd(lcm_ab, c)
        return lcm_abc

    def get_numbers(self):
        '''get generated numbers'''
        return self.numbers

    def get_lcm(self):
        '''get the least common multiple for the generated numbers'''
        return self.lcm

    def get_answer(self):
        '''get the answer as the least common multiple for the generated numbers'''
        return self.get_lcm()

    def is_correct_answer(self, answer):
        return answer == self.get_answer()
