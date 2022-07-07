import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for attr in kwargs.keys():
            self.__dict__[attr] = kwargs[attr]
        for key, value in kwargs.items():
            for k in range(value):
                self.contents.append(key)
        # print(self.contents)

    def draw(self, num_picks):
        lista = []
        if num_picks < len(self.contents):
            for i in range(num_picks):
                chosen = str(random.choice(self.contents))
                lista.append(chosen)
                self.contents.remove(chosen)
                # print(self.contents)
        else:
            for i in range(num_picks):
                chosen = random.choice(self.contents)
                lista.append(chosen)
        return lista


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    # deep or shallow copy
    balls_col = copy.copy(hat.contents)

    # balls expected to be found
    for key, value in expected_balls.items():
        for k in range(value):
            expected.append(key)
    # print(expected)

    success = 0
    for i in range(num_experiments):
        cpt = 0
        case = hat.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if case.count(key) >= value:
                cpt += 1
        if cpt == len(expected_balls):
            success += 1
    # print(success)
    return success/num_experiments
