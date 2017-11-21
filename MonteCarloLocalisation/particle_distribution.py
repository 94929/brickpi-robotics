""" Normalisation and Resampling

"""

import random
import bisect

# define global variables
nb_particles = 100
position = []

def normalise():
    total_weight = sum(weight for _, _, _, weight in position)
    for i in range(nb_particles):
        position[i] = (position[0], position[1], position[2], position[3] / total_weight)

def resample():
    # create a list which will replace position list after resampling
    new_position = []
    
    # create cumulative weights list
    cumulative_weight = []

    # insert first weight
    cumulative_weight.append(position[0][3])

    # insert the rest weights cumulatively
    for i in range(nb_particles - 1):
            curr = position[i+1]
            cumulative_weight.append(curr[3] + (cumulative_weight[-1]))

    # now, do random sampling (i.e. resampling)
    for i in range(nb_particles):
            # pick any probability (i.e. cumulative weight)
            pick = random.uniform(0,1)
            
            # find particle with that probability
            index = bisect.bisect_left(cumulative_weight, pick)
            
            # create a copy of that particle and append it to new_position array
            curr = position[index]
            tup = (curr[0], curr[1], curr[2], 1 / nb_particles)
            new_position.append(tup)

    position = new_position
