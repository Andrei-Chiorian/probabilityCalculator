import copy
import random


class Hat:
    def __init__(self, **kwargs):
        """
        This class acts as a virtual hat for the hat drawing problem.
        It takes a dictionary of ball colours and their respective amounts as input.
        The dictionary is converted into a list of balls, which are then stored in the hat.
        :param kwargs: a dictionary of balls and their respective amounts
        """
        self.contents = [key for key, value in kwargs.items() for i in range(0, value)]

    def remove(self, choice):
        """
        This method removes a ball from the hat and returns it.
        :param choice: the type of ball to be removed
        :return: the type of ball removed
        """
        try:
            self.contents.remove(choice)
            return choice
        except ValueError:
            return None

    def draw(self, number):
        """
        This method draws a number of balls from the hat and returns them.
        If the number of balls to be drawn is greater than the number of balls in the hat,
        it will return all the balls in the hat.
        :param number: the number of balls to be drawn
        :return: a list of the balls drawn
        """
        if number <= len(self.contents):
            return [self.remove(random.choice(self.contents)) for i in range(0, number)]
        else:
            drawn_contents = [item for item in self.contents]
            self.contents = []
            return drawn_contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    This function runs an experiment to estimate the probability of drawing a certain
    combination of balls from the hat. It takes a hat object, a dictionary of expected
    balls and their respective amounts, the number of balls to be drawn from the hat,
    and the number of experiments to run as parameters.
    :param hat: the hat object
    :param expected_balls: a dictionary of expected balls and their respective amounts
    :param num_balls_drawn: the number of balls to be drawn from the hat
    :param num_experiments: the number of experiments to run
    :return: the estimated probability of drawing the expected balls
    """

    num_of_success = 0  # initialize the number of successful experiments to 0

    for _ in range(0, num_experiments):  # run the experiment the specified number of times
        copied_hat = copy.deepcopy(hat)  # create a copy of the hat
        drawn_balls = copied_hat.draw(num_balls_drawn)  # draw the specified number of balls from the hat
        results = [value <= drawn_balls.count(ball) for ball, value in expected_balls.items()]
        # check if the results of the draw match the expected results
        if all(results):  # if all the results match, increment the number of successful experiments
            num_of_success += 1

    return num_of_success / num_experiments  # return the estimated probability as a decimal value
