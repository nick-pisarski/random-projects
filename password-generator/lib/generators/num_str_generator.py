from random import randint

class NumberStringGenerator():

    def get_number_str(self, len: int) -> str:
        numstr = [str(randint(0,9)) for _ in range(len)]
        return ''.join(numstr)
    
