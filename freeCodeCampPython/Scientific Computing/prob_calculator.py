import copy
import random

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = list()
        for k, v in self.balls.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, x):
        if x+1 >= len(self.contents):
            return self.contents
        result = list()
        i = 0
        while i < x:
            random_ball = random.choice(self.contents)
            result.append(self.contents.pop(self.contents.index(random_ball)))
            i += 1
        return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    for i in range(num_experiments):
        result = copy.deepcopy(hat).draw(num_balls_drawn)
        a = True
        for k, v in expected_balls.items():
            if not result.count(k) >= v: a = False
        if a: matches += 1
    return matches/num_experiments

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat_test = Hat(blue=3,red=2,green=6)
hat_test2 = Hat(yellow=5,red=1,green=3,blue=9,test=1)

# print(hat1.draw(9))

# print(experiment(hat_test, {"red":2, "green":1}, 5, 10))  
print(experiment(hat=hat_test, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=5))
# print(experiment(hat=hat_test2, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100))