import numpy as np
from scipy.interpolate import RegularGridInterpolator
import topogenesis as tg

def interpolate(info_lowres, base_highres):
    # line spaces
    x_space = np.linspace(info_lowres.minbound[0], info_lowres.maxbound[0],info_lowres.shape[0])
    y_space = np.linspace(info_lowres.minbound[1], info_lowres.maxbound[1],info_lowres.shape[1])
    z_space = np.linspace(info_lowres.minbound[2], info_lowres.maxbound[2],info_lowres.shape[2])

    # interpolation function
    interpolating_function = RegularGridInterpolator((x_space, y_space, z_space), info_lowres, bounds_error=False, fill_value=None)

    # high_res lattice
    envelope_lattice = base_highres + 1
    
    # sample points
    sample_points = envelope_lattice.centroids
    #print(envelope_lattice)
    # interpolation
    interpolated_values = interpolating_function(sample_points)

    # lattice construction
    info_highres = tg.to_lattice(interpolated_values.reshape(base_highres.shape), base_highres)

    # nulling the unavailable cells
    info_highres *= base_highres

    return info_highres

def squareness(square_weight, free_neighs, a_eval):
    free_neighs_count = []
    for free_neigh in free_neighs:
        free_neighs_count.append(free_neighs.count(free_neigh))
    a_weighted_square = np.array(free_neighs_count) ** square_weight
    a_eval *= a_weighted_square