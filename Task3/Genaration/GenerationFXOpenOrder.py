import random
import string

from GenerationOrder import GenerationOrder


class GenerationFXOpenOrder(GenerationOrder):
    
    durations = ['Immediate or cancel', 'Good Till Cancel']
    
    def __init__(self):
        pass

    def provider_generated(self):
        return '~'

    def duration_generated(self):
        return self.durations[random.randint(0, 1)]

    def comment_length_generated(self):
        return 10

    def __randstring(self):
        return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])

    def comment_generated(self):
        return self.__randstring()

    def tag_length_generated(self):
        return 10

    def tag_generated(self):
        return self.__randstring()

    def magical_number(self):
        return 100000000
