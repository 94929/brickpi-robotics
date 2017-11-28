""" Write a function navigateToWaypoint(X, Y)

"""

import math

# Let robot's initial position is (0, 0, 0)
x = 0
y = 0
theta = 0

def navigate_to_waypoint(X, Y):
    dx = X - x
    dy = Y - y

    alpha = math.atan2(dy, dx)
    beta = alpha - theta

    # TODO: implement rotate(angle_in_degree)
    rotate(beta)

    dist = math.sqrt(dx**2 + dy**2)

    # TODO: implement move(distance_in_cm)
    move(dist)

