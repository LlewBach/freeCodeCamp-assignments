import random
from collections import defaultdict
from copy import deepcopy

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

        self.contents = []
        for key, val in kwargs.items():
            self.contents.extend([key] * val)
            

    def draw(self, draw_number):
        contents_length = len(self.contents)
        if draw_number >= contents_length:
            return self.contents

        # contents_copy = self.contents[:]
        drawn_list = []
        for x in range(draw_number):
            ran_index = random.randint(0, contents_length - 1) 
            drawn_list.append(self.contents[ran_index])
            self.contents.pop(ran_index)
            contents_length -= 1
        return drawn_list

        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        all_present = True
        hat_copy = deepcopy(hat)
        drawn_balls_list = hat_copy.draw(num_balls_drawn)
        drawn_dict = defaultdict(int)
        for ball in drawn_balls_list:
            drawn_dict[ball] += 1
        for key, val in expected_balls.items():
            if val > drawn_dict[key]:
                all_present = False
                break
        if all_present == True:
            m += 1
    return m / num_experiments
        