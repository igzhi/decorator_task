from datetime import datetime
from decor_task import make_trace

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

@make_trace
def flat_generator(a: list) -> list:
    return [x for sublist in a for x in sublist]

flat_generator(nested_list)
