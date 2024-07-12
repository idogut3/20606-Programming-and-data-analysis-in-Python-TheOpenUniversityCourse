from data_analysis import *
from data_preparation import *
from data_display import *

if __name__ == '__main__':
    # Exercise: A
    data = load_data('nasa.csv')

    # Exercise: B
    names = ['Est Dia in Miles(min)', 'Est Dia in Miles(max)', 'Est Dia in Feet(min)', 'Est Dia in Feet(max)']
    scoped_data_array = scoping_data(data, names)

    # Exercise: C
    masked_data = mask_data(data)

    # Exercise: D
    after_data_details_array = data_details(data)

    # Exercise: E
    max_absolute_mag_tuple = max_absolute_magnitude(data)

    # Exercise: F
    closest_to_earth_asteroid_name = closest_to_earth(data)

    # Exercise: G
    common_orbit_dict = common_orbit(data)

    # Exercise: H
    min_max_diameter_tuple = min_max_diameter(data)

    # Exercise: I
    plt_hist_diameter(data)

    # Exercise: J
    plt_hist_common_orbit(data)

    # Exercise: K
    plt_pie_hazard(data)

    # Exercise: L
    plt_liner_motion_magnitude(data)
