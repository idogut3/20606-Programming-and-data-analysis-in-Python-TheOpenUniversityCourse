import numpy as np
from scipy import stats

"""
    @function max_absolute_magnitude

    :param data: np.ndarray

    @description:
    The function gets data, an np.ndarray containing a table of rows and columns with data inside of them.
    It returns a tuple where the first member contains the name of the asteroid (Name) with the maximum proximity size
    (Absolute Magnitude) in relation to the distance to the Earth and the second member (of the tuple),
    contains the magnitude value.

    :returns a tuple 
"""


def max_absolute_magnitude(data: np.ndarray) -> tuple:
    absolute_magnitude_title = 'Absolute Magnitude'
    name_of_asteroid_column_title = 'Name'

    try:  # Trying to find the indexes for each column title
        index_of_absolute_magnitude_title = np.where(data[0] == absolute_magnitude_title)[0][0]
        index_of_name_title = np.where(data[0] == name_of_asteroid_column_title)[0][0]

    except IndexError:  # Did not find at least one of the columns with the specified names we gave
        raise ValueError(
            f"Column '{absolute_magnitude_title}' or '{name_of_asteroid_column_title}' not found in the data.")

    max_distance = float(data[1][index_of_absolute_magnitude_title])
    max_distance_index = 1

    # Looping through all the max_distances of each asteroid and checking to see which is the largest
    # 2 is because we do not include the title name (because we are trying to find the values not the string title duh,
    # and we start out with the comparing from the second element because our first element is the first value we
    # compare from ie: we do not compare arr[1] to arr[1] because it is a wasted action, so we compare arr[1] to arr[2]
    for i in range(2, len(data)):
        current_value = float(data[i][index_of_absolute_magnitude_title])
        if current_value > max_distance:
            max_distance = current_value
            max_distance_index = i

    name_with_max_dist = data[max_distance_index][index_of_name_title]
    return int(name_with_max_dist), max_distance


"""
    @function closest_to_earth

    :param data: np.ndarray

    @description:
    The function gets data, an np.ndarray containing a table of rows and columns with data inside of them.
    It returns the name of the asteroid (Name) the closest to the earth according to its distance from the earth in km 
    Miss Dist. (kilometers).

    :returns int (the name of the asteroid 
"""


def closest_to_earth(data: np.ndarray):
    distance_from_earth_in_km_title = 'Miss Dist.(kilometers)'
    name_of_asteroid_column_title = 'Name'

    try:  # Trying to find the indexes for each column title
        index_of_miss_dist_in_kilometers = np.where(data[0] == distance_from_earth_in_km_title)[0][0]
        index_of_name_title = np.where(data[0] == name_of_asteroid_column_title)[0][0]
    except IndexError:  # Did not find at least one of the columns with the specified names we gave
        raise ValueError(
            f"Column '{distance_from_earth_in_km_title}' or '{name_of_asteroid_column_title}' not found in the data.")

    min_distance = float(data[1][index_of_miss_dist_in_kilometers])
    min_distance_index = 1

    # Looping through all the distances from earth in km value for each asteroid and checking to see which is the 
    # closest to earth.
    # 2 is because we do not include the title name (because we are trying to find the values not the string title duh,
    # and we start out with the comparing from the second element because our first element is the first value we
    # compare from ie: we do not compare arr[1] to arr[1] because it is a wasted action, so we compare arr[1] to arr[2]
    for i in range(2, len(data)):
        current_value = float(data[i][index_of_miss_dist_in_kilometers])
        if current_value < min_distance:
            min_distance = current_value
            min_distance_index = i

    name_with_min_dist = data[min_distance_index][index_of_name_title]
    return int(name_with_min_dist)


"""
    @function common_orbit

    :param data: np.ndarray

    @description:
    The function gets data, an np.ndarray containing a table of rows and columns with data inside of them.
    It returns a dictionary (dict) where the key for each value is the orbit ID (Orbit ID) and the value is the amount
    of asteroids in each orbit.

    :returns dict
"""


def common_orbit(data: np.ndarray) -> dict:
    # Define the title of the column we're interested in
    orbit_id_column_title = 'Orbit ID'

    try:  # Trying to find the index of the 'Orbit ID' column
        column_index = np.where(data[0] == orbit_id_column_title)[0][0]
    except IndexError:  # Did not find the index of the column's title with the specified name for the orbit_id 
        raise ValueError(f"Column '{orbit_id_column_title}' not found in the data.")

    # Extract the 'Orbit ID' column values (excluding the header)
    column_orbit_id_values = data[1:, column_index]

    # Count occurrences using a dictionary
    value_counts = {}
    for value in column_orbit_id_values:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    # Creating a dict with the corrected values for each key  orbit ID (Orbit ID) it's value (amount of asteroids in 
    # each orbit) 
    orbit_id_amount_of_asteroids_per_orbit_dictionary = {str(key): value for key, value in value_counts.items()}

    return orbit_id_amount_of_asteroids_per_orbit_dictionary


"""
    @function min_max_diameter

    :param data: np.ndarray

    @description: The function gets data, an np.ndarray containing a table of rows and columns with data inside of 
    them. and returns a tuple that in it the first member is the average value of the minimum diameter per km and and 
    the second member is the average value of the maximum diameter per km among all the asteroids in the data set. 


    :returns tuple
"""


def min_max_diameter(data: np.ndarray) -> tuple:
    average_value_of_the_minimum_diameter_per_km_title_name = 'Est Dia in KM(min)'
    average_value_of_the_maximum_diameter_per_km_title_name = 'Est Dia in KM(max)'
    min_sum = 0
    max_sum = 0

    try:  # Trying to find the indexes for each column title
        index_of_est_dia_in_km_min = np.where(data[0] == average_value_of_the_minimum_diameter_per_km_title_name)[0][0]
        index_of_est_dia_in_km_max = np.where(data[0] == average_value_of_the_maximum_diameter_per_km_title_name)[0][0]
    except IndexError:  # Did not find at least one of the columns with the specified names we gave
        raise ValueError(
            f"Column '{average_value_of_the_minimum_diameter_per_km_title_name}' or '{average_value_of_the_maximum_diameter_per_km_title_name}' not found in the data.")

    # Calculating the averages with a for loop
    for i in range(1, len(data)):
        min_sum += float(data[i][index_of_est_dia_in_km_min])
        max_sum += float(data[i][index_of_est_dia_in_km_max])
    return min_sum / (len(data) - 1), max_sum / (len(data) - 1)


"""
    @function is_there_linear_relationship_between_absolute_magnitude_to_velocity_of_asteroid

    :param magnitudes: list of magnitudes
    :param velocities: list of velocities

    @description: 
    The function calculates if there is a linear relationship between the magnitudes and the velocity of each magnitude,
    if there is such a relationship it returns True, otherwise False.
    It checks to see if the p_value calculated by the scipy.stats library lingress function between the magnitudes and
    the velocities is smaller then 0.05. If it is smaller there is such a linear relationship hence it returns True,
    otherwise there is not a linear relationship (Though there might be a different relationship) so it returns False.

    :returns bool
"""


def is_there_linear_relationship_between_absolute_magnitude_to_velocity_of_asteroid(magnitudes, velocities) -> bool:
    # Calculating all the values for the linear regression using the scipy.stats library
    a, b, r_value, p_value, std_err = stats.linregress(magnitudes, velocities)
    if p_value < 0.05:  # There is a linear relationship between the absolute magnitude to the velocity of the asteroid
        return True
    return False
