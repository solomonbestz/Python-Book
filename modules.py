# PYTHON MODULE

from calculation import add_calc

if __name__=="__main__":
    # print(add_calc(34, 50))
    pass


# RANDOM MODULE 

import random


if __name__=='__main__':

    my_list = [1, 2, 6, 5, 9, 3]

    rand_item = random.choice(my_list)
    print(rand_item)

    rand_num = random.randint(1, 10)

    