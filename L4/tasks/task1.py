import random
from string import ascii_lowercase

def generate_random_strings(num_strings, string_length):
    for _ in range(num_strings):
        yield ''.join(random.choice(ascii_lowercase) for _ in range(string_length))


'''
random_strings = generate_random_strings(1_000_000, 10)
for i, string in enumerate(random_strings):
    if i < 5:
        print(string)
    else:
        break
        '''
