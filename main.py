from data_analysis import *
from data_preparation import *
from date import *
from data_display import *

if __name__ == '__main__':
    # Exercise: A
    data = load_data('nasa.csv')
    print(data)

    # Exercise: B
    print('\n\n\n', 'Before (exercise B):')
    print(data)

    print('\n\n\n', 'After (exercise B):')
    names = ['Est Dia in Miles(min)', 'Est Dia in Miles(max)', 'Est Dia in Feet(min)', 'Est Dia in Feet(max)']
    scoped_data_array = scoping_data(data, names)
    print(scoped_data_array)

    # Exercise: C
    print('\n\n\n', 'Before (exercise C):')
    print(data)

    print('\n\n\n', 'After (exercise C):')
    masked_data = mask_data(data)
    print(masked_data)

    # Exercise: D
    print('\n\n\n', 'Before (exercise D):')
    print(data)

    print('\n\n\n', 'After (exercise D):')
    after_data_details_array = data_details(data)
    print(after_data_details_array)

    # Exercise: E
    print('\n\n\nExercise: E')
    max_absolute_mag_tuple = max_absolute_magnitude(data)
    print(max_absolute_mag_tuple)

    # Exercise: F
    print('\n\n\nExercise: F')
    closest_to_earth_asteroid_name = closest_to_earth(data)
    print(closest_to_earth_asteroid_name)

    # Exercise: G
    print('\n\n\nExercise: G')
    common_orbit_dict = common_orbit(data)
    print(common_orbit_dict)

    # Exercise: H
    print('\n\n\nExercise: H')
    min_max_diameter_tuple = min_max_diameter(data)
    print(min_max_diameter_tuple)

    # Exercise: I
    plt_hist_diameter(data)

    # Exercise: J
    plt_hist_common_orbit(data)

    # Exercise: K
    plt_pie_hazard(data)

    # Exercise: L
    plt_liner_motion_magnitude(data)
