import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from data_analysis import min_max_diameter
from data_preparation import load_data
from data_analysis import is_there_linear_relationship_between_absolute_magnitude_to_velocity_of_asteroid

"""
    @function plt_hist_diameter

    :param data: np.ndarray

    @description:
    The function gets data, an np.ndarray containing a table of rows and columns with data inside of them.
    It displays a histogram graph of the amount of asteroids according to their average diameter per km.
    The graph includes 10 Diameter averages which ranges between the minimum average diameter value per km to 
    the maximum average diameter value per km.
"""


def plt_hist_diameter(data: np.ndarray):
    # Setting the titles
    plt.title('The amount of asteroids according to their average diameter per km')
    plt.xlabel('Average diameter (in km)')
    plt.ylabel('Number of asteroids')

    # Getting the tuple containing the minimum_average_diameter_value_per_km and
    # the maximum_average_diameter_value_per_km
    min_max_diameter_tuple = min_max_diameter(data)
    minimum_average_diameter_value_per_km = min_max_diameter_tuple[0]
    maximum_average_diameter_value_per_km = min_max_diameter_tuple[1]

    num_of_bins = 10
    num_of_edges = num_of_bins + 1
    bins = np.linspace(minimum_average_diameter_value_per_km, maximum_average_diameter_value_per_km, num_of_edges)

    minimum_diameter_value_per_km_title_name = 'Est Dia in KM(min)'
    maximum_diameter_value_per_km_title_name = 'Est Dia in KM(max)'

    try:  # Trying to find the indexes for each column title
        index_of_est_dia_in_km_min = np.where(data[0] == minimum_diameter_value_per_km_title_name)[0][0]
        index_of_est_dia_in_km_max = np.where(data[0] == maximum_diameter_value_per_km_title_name)[0][0]
    except IndexError:  # Did not find at least one of the columns with the specified names we gave
        raise ValueError(
            f"Column '{minimum_diameter_value_per_km_title_name}' or '{maximum_diameter_value_per_km_title_name}' not "
            f"found in the data.")

    average_diameters = []

    # Calculating the averages
    for i in range(1, len(data)):
        current_asteroid_min_diameter = float(data[i][index_of_est_dia_in_km_min])
        current_asteroid_max_diameter = float(data[i][index_of_est_dia_in_km_max])
        current_asteroid_average_diameter = (current_asteroid_min_diameter + current_asteroid_max_diameter) / 2
        average_diameters.append(current_asteroid_average_diameter)

    # Drawing the graph
    plt.hist(average_diameters, bins=bins, edgecolor='black')
    plt.grid(True)
    plt.show()


"""
    @function plt_hist_common_orbit

    :param data: np.ndarray

    @description:
    The function gets data, an np.ndarray containing a table of rows and columns with data inside of them.
    It displays a histogram graph of the amount of asteroids according to their orbit. 
    There are different 6 track ranges starting from the minimum track value to the maximum track value.
"""


def plt_hist_common_orbit(data: np.ndarray):
    # Setting the titles
    plt.title('Histogram of asteroid by minimum orbit intersection')
    plt.xlabel('Minimum orbit intersection')
    plt.ylabel('Number of asteroids')

    orbit_id_column_title = 'Orbit ID'

    try:  # Trying to find the indexes for the column title
        column_index = np.where(data[0] == orbit_id_column_title)[0][0]
    except IndexError:  # Did not find the index of the column's title with the specified name for the orbit_id
        raise ValueError(f"Column '{orbit_id_column_title}' not found in the data.")

    # Extract the 'Orbit ID' column values (excluding the header)
    orbit_id_column_values = data[1:, column_index].astype(float)
    min_orbit = np.min(orbit_id_column_values)
    max_orbit = np.max(orbit_id_column_values)

    # Define the bins for the histogram
    num_of_bins = 6
    num_of_edges = num_of_bins + 1
    bins = np.linspace(min_orbit, max_orbit, num_of_edges)  # 6 bins means 7 edges

    # Drawing the graph
    plt.hist(orbit_id_column_values, bins=bins, edgecolor='black')
    plt.grid(True)
    plt.show()


"""
    @function plt_pie_hazard

    :param data: np.ndarray

    @description:
     The function gets data, an np.ndarray containing a table of rows and columns with data inside of them.
     It displays the percentages of the the hazardous and non-hazardous asteroids according to the classification 
     of the Hazardous column in the data array in a pie graph.
"""


def plt_pie_hazard(data: np.ndarray):
    # Setting the title
    plt.title('Percentage of hazardous and non-hazardous asteroids')

    hazardous_column_title = 'Hazardous'
    try:  # Trying to find the indexes for the column title
        column_index = np.where(data[0] == hazardous_column_title)[0][0]
    except IndexError:  # Did not find the index of the column's title with the specified name
        raise ValueError(f"Column '{hazardous_column_title}' not found in the data.")

    # Extract the 'Hazardous' column values (excluding the header)
    hazardous_column_values = data[1:, column_index]

    # Count occurrences of 'True' and 'False' in the 'Hazardous' column
    unique, counts = np.unique(hazardous_column_values, return_counts=True)
    counts_dict = dict(zip(unique, counts))

    # Get counts of hazardous and non-hazardous asteroids
    hazardous_count = counts_dict.get('True', 0)
    non_hazardous_count = counts_dict.get('False', 0)

    # Define the labels, colors and sizes for the pie chart
    labels = ['Hazardous', 'Non-Hazardous']
    colors = ['red', 'green']
    sizes = [hazardous_count, non_hazardous_count]

    # Drawing the pie chart
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.show()


"""
    @function plt_liner_motion_magnitude

    :param data: np.ndarray

    @description:
     The function gets data, an np.ndarray containing a table of rows and columns with data inside of them.
     It checks whether there is a linear relationship between the magnitude of the maximum sacrifice to the Earth 
     (Absolute Magnitude) of each asteroid to it's speed of movement (Miles per hour).
     It prints out the result (True or False) and also draws up the graph.
     (the linear regression graph with the points and the line displaying the relationship).
"""


def plt_liner_motion_magnitude(data: np.ndarray):
    # Setting the titles
    plt.title('Linear regression graph displaying the relationship between absolute magnitude and miles per hour')
    plt.xlabel('Absolute magnitude')
    plt.ylabel('Velocities (miles per hour)')

    # Extract column titles
    title_magnitude = 'Absolute Magnitude'
    title_velocity = 'Miles per hour'

    try:  # Trying to find the indexes for each column title
        index_magnitude = np.where(data[0] == title_magnitude)[0][0]
        index_velocity = np.where(data[0] == title_velocity)[0][0]
    except IndexError:  # Did not find at least one of the columns with the specified names we gave
        raise ValueError(f"Columns '{title_magnitude}' or '{title_velocity}' not found in the data.")

    # Extract data values from the columns (excluding header)
    magnitudes = data[1:, index_magnitude].astype(float)
    velocities = data[1:, index_velocity].astype(float)

    # Checking to see if there is a linear relationship between the absolute magnitude to the velocity of the asteroid
    is_there_linear_relationship_between_the_absolute_magnitude_to_velocity_of_asteroid = \
        is_there_linear_relationship_between_absolute_magnitude_to_velocity_of_asteroid(
            magnitudes=magnitudes,
            velocities=velocities)

    print('Is there a linear relationship between the absolute magnitude to the velocity of the asteroid')

    if is_there_linear_relationship_between_the_absolute_magnitude_to_velocity_of_asteroid:
        print('Yes, there is a linear relationship between the absolute magnitude to the velocity of the asteroid')
    else:
        print(
            'No, there is no linear relationship between the absolute magnitude to the velocity of the asteroid but '
            'there could be a non linear one')

    # Calculating the graph we need to show
    a, b, r_value, p_value, std_err = stats.linregress(magnitudes, velocities)

    r_value_rounded = round(r_value, 2)
    plt.scatter(magnitudes, velocities, label='Data points')  # Drawing all the points on the graph
    plt.plot(magnitudes, a * magnitudes + b, color='red', label=f'Fitted line r={r_value_rounded}')  # Drawing the line

    plt.legend(loc="upper right")
    plt.show()
