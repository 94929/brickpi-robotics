""" Point estimate of the current position and orientation of the robot

"""

# take mean of all particles
def estimate_point(position):
    x = 0
    y = 0
    theta = 0

    for pos in position:
        w = pos[3]
        
        x += pos[0] * w
        y += pos[1] * w
        theta += pos[2] * w

    return x, y, theta
