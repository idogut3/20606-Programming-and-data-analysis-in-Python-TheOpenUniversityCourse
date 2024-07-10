import numpy as np
from scipy import stats


def max_absolute_magnitude(data: np.ndarray) -> tuple:
    title = 'Absolute Magnitude'
    title1 = 'Name'

    try:
        index_of_absolute_magnitude_title = np.where(data[0] == title)[0][0]
        index_of_name_title = np.where(data[0] == title1)[0][0]
    except IndexError:
        raise ValueError(f"Column '{title}' or '{title1}' not found in the data.")

    max_dist = float(data[1][index_of_absolute_magnitude_title])
    max_dist_index = 1

    for i in range(2, len(data)):
        current_value = float(data[i][index_of_absolute_magnitude_title])
        if current_value > max_dist:
            max_dist = current_value
            max_dist_index = i

    name_with_max_dist = data[max_dist_index][index_of_name_title]
    return int(name_with_max_dist), max_dist


def closest_to_earth(data: np.ndarray):
    title = 'Miss Dist.(kilometers)'
    title1 = 'Name'

    try:
        index_of_miss_dist_in_kilometers = np.where(data[0] == title)[0][0]
        index_of_name_title = np.where(data[0] == title1)[0][0]
    except IndexError:
        raise ValueError(f"Column '{title}' or '{title1}' not found in the data.")

    min_dist = float(data[1][index_of_miss_dist_in_kilometers])
    min_dist_index = 1

    for i in range(2, len(data)):
        current_value = float(data[i][index_of_miss_dist_in_kilometers])
        if current_value < min_dist:
            min_dist = current_value
            min_dist_index = i

    name_with_min_dist = data[min_dist_index][index_of_name_title]
    return int(name_with_min_dist)


def common_orbit(data: np.ndarray) -> dict:
    # Define the title of the column we're interested in
    column_title = 'Orbit ID'

    try:
        # Find the index of the 'Orbit ID' column
        column_index = np.where(data[0] == column_title)[0][0]
    except IndexError:
        raise ValueError(f"Column '{column_title}' not found in the data.")

    # Extract the 'Orbit ID' column values (excluding the header)
    column_values = data[1:, column_index]

    # Count occurrences using a dictionary
    value_counts = {}
    for value in column_values:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    converted_dict = {str(key): value for key, value in value_counts.items()}

    return converted_dict


def min_max_diameter(data: np.ndarray) -> tuple:
    title = 'Est Dia in KM(min)'
    title1 = 'Est Dia in KM(max)'
    min_sum = 0
    max_sum = 0

    try:
        index_of_est_dia_in_km_min = np.where(data[0] == title)[0][0]
        index_of_est_dia_in_km_max = np.where(data[0] == title1)[0][0]
    except IndexError:
        raise ValueError(f"Column '{title}' or '{title1}' not found in the data.")

    for i in range(1, len(data)):
        min_sum += float(data[i][index_of_est_dia_in_km_min])
        max_sum += float(data[i][index_of_est_dia_in_km_max])
    return min_sum / (len(data) - 1), max_sum / (len(data) - 1)


def is_there_linear_relationship_between_absolute_magnitude_to_velocity_of_asteroid(magnitudes, velocities) -> bool:
    a, b, r_value, p_value, std_err = stats.linregress(magnitudes, velocities)

    if p_value < 0.05:  # There is a linear relationship between the absolute magnitude to the velocity of the asteroid
        return True
    return False
