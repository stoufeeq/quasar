# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x^2 + y^2 = r^2.

# circle within the square of unit length.
# area of square = 1 (points in square)
# area of circle = π*(1/2)^2 = π/4  (points in circle)
# π = 4*(points in circle)/(points in square)

# x^2 + y^2 = r^2, so if r < 1, the point is inside the circle
# calculate x*x + y*y and if it is less than 1, then increment the counter for circle points

import random


def pi_generator(iterations):

    circle_counter = 0
    square_counter = 0

    while square_counter < iterations:
        rand_x = random.uniform(0, 1)
        rand_y = random.uniform(0, 1)
        if rand_x*rand_x + rand_y*rand_y <= 1:
            circle_counter += 1
        square_counter += 1

    return 4*(circle_counter/square_counter)


print("pi = ", "%.3f" % pi_generator(9999999))
