import numpy as np
import matplotlib.pyplot as plt

from data_analysis import min_max_diameter
from data_preparation import load_data


def plt_hist_diameter(data: np.ndarray):
    # Setting the titles
    plt.title('The amount of asteroids according to their average diameter per km')
    plt.xlabel('Average diameter (in km)')
    plt.ylabel('Number of asteroids')

    min_max_diameter_tuple = min_max_diameter(data)
    minimum_average_diameter_value_per_km = min_max_diameter_tuple[0]
    maximum_average_diameter_value_per_km = min_max_diameter_tuple[1]

    bins = np.linspace(minimum_average_diameter_value_per_km, maximum_average_diameter_value_per_km, 11)

    title_min = 'Est Dia in KM(min)'
    title_max = 'Est Dia in KM(max)'

    try:
        index_of_est_dia_in_km_min = np.where(data[0] == title_min)[0][0]
        index_of_est_dia_in_km_max = np.where(data[0] == title_max)[0][0]
    except IndexError:
        raise ValueError(f"Column '{title_min}' or '{title_max}' not found in the data.")

    average_diameters = []

    for i in range(1, len(data)):
        min_dia = float(data[i][index_of_est_dia_in_km_min])
        max_dia = float(data[i][index_of_est_dia_in_km_max])
        avg_dia = (min_dia + max_dia) / 2
        average_diameters.append(avg_dia)

    plt.hist(average_diameters, bins=bins, edgecolor='black')
    plt.grid(True)
    plt.show()


# def plt_hist_common_orbit(data: np.ndarray):


if __name__ == '__main__':
    data = load_data('nasa.csv')
    plt_hist_diameter(data)
