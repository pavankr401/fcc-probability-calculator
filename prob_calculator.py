import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = []

        # push the number of balls of each color into the contents
        for key in kwargs:
            for i in range(kwargs[key]):
                self.contents.append(key)

    def draw(self, num_of_balls):
        if (num_of_balls > len(self.contents)):
            return self.contents

        selected_balls = []
        for i in range(num_of_balls):
            random_num = random.randrange(0, len(self.contents))
            selected_balls.append(self.contents.pop(random_num))

        return selected_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    # number of times that expected balls came
    M = 0
    # number of experiments
    N = num_experiments
    
    # draw the balls from  the hat and store in the balls_drawn
    # calculate the frequency to the drawn balls and compare to the expected_balls
    # if it matches the expected ball increment the M 
    for i in range(N):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_drawn_freq = {}
        for ball in balls_drawn:
            balls_drawn_freq[ball] = balls_drawn_freq.get(ball, 0) + 1
        # print(balls_drawn_freq)
        
        # check the balls freq that are coming as expected or not
        match = True
        for ball in expected_balls:
            if(ball not in balls_drawn_freq or balls_drawn_freq[ball] < expected_balls[ball]):
                match = False
                break
        
        if(match):
            M += 1
    
    res = M/N
    return res

# hat = Hat(blue=3,red=2,green=6)
# probability = experiment(hat=hat,
#                          expected_balls={"blue": 2, "green": 1},
#                          num_balls_drawn=4,
#                          num_experiments=1000)

# print(probability)