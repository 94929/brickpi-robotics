""" Representing and Displaying Uncertain Motion with a Particle Set

"""

import random
import math

NUMBER OF PARTICLES = nb_particles = 100
weight = w = 1 / nb_particles

# init_normal_distribution_variables(mu, sigma)
mu = 0
sigma = 0.01

# position, contains all particles represeting posible locations of the robot.
position = []
weights = []

# init_postion(starting_position)
def init_position(pos):
    position = pos * nb_particles

def init_weights():
    weights = weight * nb_particles

# update_particles_in_position(D)
def update_particles_with_D(D):
    
    # init_distance_noise_terms(e, f)
    e = f = random.gauss(mu, sigma)
    
    # iterate_all_particles_in_position()
    for i in range(nb_particles):
        curr = position[i]

        currX = curr[0]
        currY = curr[1]
        currT = curr[2]
        
        # calculate_new_particle_to_be_inserted(position[i])
        newX = currX + (D + e) * math.cos(currT)
        newY = currY + (D + e) * math.sin(currT)
        newT = currT + f

        # replace_old_particle(updated_particle)
        position[i] = (newX, newY, newT)

def update_particles_with_A(A):
    
    # init_angular_noise_terms(g)
    g = random.gauss(mu, sigma)

    for i in range(nb_particles):
        curr = position[i]

        currX = curr[0]
        currY = curr[1]
        currT = curr[2]

        position[i] = (currX, currY, currT + A + g)

# init_canvas_on_web_interface
def init_web_canvas():
    line1 = (100, 100, 500, 100)
    line2 = (500, 100, 500, 500)
    line3 = (500, 500, 100, 500)
    line4 = (100, 500, 100, 100)
    
    print 'drawLine: ' + str(line1)
    print 'drawLine: ' + str(line2)
    print 'drawLine: ' + str(line3)
    print 'drawLine: ' + str(line4)

# draw_current_particles_in_position()
def draw_particles():
    print 'drawParticles: ' + str(position)

