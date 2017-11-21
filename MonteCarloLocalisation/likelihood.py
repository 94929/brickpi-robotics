import math

# from drwaing module, import mymap
from drawing import mymap

""" This function returns a probability, tells us how reliable given particle is.

    1. it needs to find out which wall the sonar beam would hit when robot is at (x, y, theta)
    2. it needs to look at the difference between m and the actual measurement z 
    2. and calculate a likelihood value, probably using a Gaussian model 

"""

# define global values to be used when calculating 
std = 3
k = 0.1

def calculate_likelihood(x, y, theta, z):
    
    # create a list that will hold all valid walls 
    walls = []

    # for each wall in mymap.walls(i.e. environment)
    for wall in mymap.walls:
        Ax = wall[0]
        Ay = wall[1]
        Bx = wall[2]
        By = wall[3]

        # calculate m (i.e. the distance between robot and the wall) value for each wall
        numerator   = (By - Ay) * (Ax - x) - (Bx - Ax) * (Ay - y)
        denominator = (By - Ay) * math.cos(theta) - (Bx - Ax) * math.sin(theta)

        # if there is no intersection between robot and the wall (i.e. sonar beam would not hit)
        if denominator == 0:
            continue

        m = numerator / denominator

        # if m is negative, the robot is not facing given wall, no need to proceed with this wall
        if m < 0:
            continue

        # get position of the possible intersection between robot and the wall
        pos_x_wall = m + math.cos(theta)
        pos_y_wall = m + math.sin(theta)

        # check if the position lies on the wall
        
        # check if intersection_x lies on the wall, 'wall'
        if (pos_x_wall >= Ax and pos_x_wall <= Bx) or (pos_x_wall <= Ax and pos_x_wall >= Bx):
            
            # check if intersection_y lies on the wall, 'wall'
            if (pos_y_wall >= Ay and pos_y_wall <= By) or (pos_y_wall <= Ay and pos_y_wall >= By):
                
                # check if the angle, beta is reasonable
                # an angle is reasonable if it lies between -30 and 30 in degree
                if (-0.525 < calculate_beta(Ax, Ay, Bx, By, theta) < 0.525):
                    
                    # then the position lies on the wall, add current (wall, distance) into the container
                    curr = (wall, m)
                    walls.append(curr)
    
    # if walls list is empty, current particle is not reliable, return probability 0 for current particle
    if not walls:
        return 0.0

    # in the obtained walls, find minimum m value
    min_m = min(walls, key = lambda x: x[1])[0]
    
    # now, calculate likelihood probability
    numerator   = -((z - m) ** 2)
    denominator = 2 * (std ** 2)
    return math.exp(numerator / denominator) + k


def calculate_beta(Ax, Ay, Bx, By, theta):
    numerator   = math.cos(theta) * (Ay-By) + math.sin(theta) * (Bx-Ax)
    denominator = math.sqrt((Ay - By)**2 + (Bx - Ax)**2)
    return math.acos(numerator / denominator)
