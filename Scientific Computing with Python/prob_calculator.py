import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.balls = {}
        # adds the ball colour and count to a dict
        for arg_name in balls:
            self.balls.update({str(arg_name):balls[arg_name]})
        # makes a list of the colour of balls * the amount of that colour
        self.contents = []
        for key,val in self.balls.items():
            self.contents.append(key)
            if val > 1:
                self.contents.extend([key] * (val - 1))

    # removes balls from the bag at random
    def draw(self, number=0):
        self.number = number
        self.removed = []
        for i in range(self.number):
            random.shuffle(self.contents)
            if len(self.contents) > 0:
                num = random.randint(range(len(self.contents)))
                count = self.contents.pop(num)
                self.removed.append(count)
        return self.removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_bag = []
    for key, val in expected_balls.items():
        expected_bag.append(key)
        if val > 1:
            expected_bag.extend([key] * (val - 1))
    expected_bag.sort()

    # takes a number of balls from the bag checks if they are the same as the expected balls
    # then calculates a probability
    count = 0
    results = []
    for i in range(num_experiments):
        removed = []
        bag = copy.copy(hat.contents)
        for j in range(num_balls_drawn):
            if len(bag)>0:
                rand_num = random.randint(0, len(bag)-1)
                num = bag.pop(rand_num)
                removed.append(num)
        removed.sort()
        results.append(removed)

        # checks whether the removed balls are in the expected balls
        if all(True if expected_bag.count(item) <= removed.count(item) else False for item in expected_bag):
            count += 1

    return count / num_experiments
