## THIS NEEDS A FIX, IT'S NOT WORKING
##
##
##
##

import copy
import random

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = list(self.balls.keys())

    def draw(self, x):
        if x+1 >= sum(self.balls.values()):
            return self.balls
        new_dict = copy.deepcopy(self.balls)
        new_list = copy.deepcopy(self.contents)
        result = dict()
        i = 0
        while i < x:
            random_ball = random.choice(self.contents)
            if(self.balls.get(random_ball) <= 0):
                self.contents.pop(self.contents.index(random_ball))
                continue
            self.balls[random_ball] -= 1
            result[random_ball] = result.get(random_ball, 0) + 1
            i += 1
        return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    for i in range(num_experiments):
        result = hat.draw(num_balls_drawn)
        a = True
        for k, v in expected_balls.items():
            if result.get(k, 0) >= v: a = False
        if a: matches += 1
    return matches/num_experiments

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat_test = Hat(blue=3,red=2,green=6)

# print(experiment(hat_test, {"red":2, "green":1}, 5, 10))

print(experiment(hat=hat_test, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=5))