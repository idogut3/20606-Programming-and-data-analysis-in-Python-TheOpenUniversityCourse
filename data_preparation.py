import numpy as np

from date import Date

"""
    @function load_data
    
    :param file_name: str
    
    @description:
    The function gets a file name and returns an array (of type ndarray) containing the data inside of the file called
    file name. The function only accepts files that are called 'nasa.csv'.
    
    Assumption:
    The file nasa.csv is in the project folder together with the python file of this project.
    
    :returns np.ndarray containing the the data inside of the file called file name.
"""


def load_data(file_name: str) -> np.ndarray:
    if file_name != 'nasa.csv':
        raise ValueError("File name must be nasa.csv")

    try:
        data = np.loadtxt(file_name, dtype=str, delimiter=',')
        return data
    except FileNotFoundError:
        raise FileNotFoundError("Cant find nasa.csv in your project, check your project resources")
    except FileExistsError:
        raise FileExistsError(
            "Error with file, cannot read it (might be useful to check if the number of rows are equal to number of "
            "columns)")
    except Exception as e:
        raise Exception(f"file error, an exception occurred: {e}")


"""
    @function scoping_data

    :param data: np.ndarray
    :param names: list

    @description:
    The function gets data, an np.ndarray containing a table of rows and columns with data inside of them and a list
    names, containing names of columns in the data table.
    The function will return an updated array without the columns with the names
    
    :returns updated np.ndarray array without the columns with the names specified
"""


def scoping_data(data: np.ndarray, names: list) -> np.ndarray:
    for name in names:  # Lopping through the list of names (That we need to deleter their columns)

        # Finding out the title of each column we want to delete (Might be more
        # than 1 column with the same name we want to delete if someone inserted it incorrectly)
        names_of_titles_of_columns_to_delete = np.where(data[0] == name)

        # Deleting all the columns that we were asked to delete by their title along the y_axis
        y_axis = 1
        data = np.delete(data, names_of_titles_of_columns_to_delete, y_axis)
    return data


"""
    @function mask_data

    :param data: np.ndarray

    @description:
    The function gets data, an np.ndarray containing a table of rows and columns with data inside of them.
    It will update and return an array with all the asteroids whose Date Approach Close (Date Approach Close)
    to earth is from 2000 onwards. 

    :returns np.ndarray with all the asteroids whose Date Approach Close (Date Approach Close)
    to earth is from 2000 onwards
"""


def mask_data(data: np.ndarray) -> np.ndarray:
    title = 'Close Approach Date'
    threshold_date = Date("2000-01-01")
    index_of_close_approach_date = np.where(data[0] == title)

    values_to_compare_threshold_date = data[:, index_of_close_approach_date]

    # Convert the dates in the "Close Approach Date" column to Date objects
    dates = [Date(values_to_compare_threshold_date[date_index][0][0]) for date_index in
             range(1, len(values_to_compare_threshold_date))]
    mask = np.array([(dates[i].year_difference(threshold_date) >= 0) for i in range(len(dates))])

    x_axis = 0
    data = np.delete(data, np.where(~mask)[0] + 1, x_axis)
    return data


"""
    @function data_details

    :param data: np.ndarray

    @description:
    The function gets data, an np.ndarray containing a table of rows and columns with data inside of them.
    It will clear the array from the the following columns: ID Reference Neo, Body Orbiting and Equinox. 
    Then, print in standard output the following data (after the update):
    1) Number of rows (rows) and number of columns (columns) existing in the array
    2) The table titles

    :returns np.ndarray updated after removal of all the following columns 'ID Reference Neo', 'Body Orbiting' and 
    'Equinox'.
"""


def data_details(data: np.ndarray) -> np.ndarray:
    titles_to_delete = ['Neo Reference ID', 'Orbiting Body', 'Equinox']

    for title in titles_to_delete:
        index_of_title_to_delete = np.where(data[0] == title)
        data = np.delete(data, index_of_title_to_delete, 1)

    rows = len(data)
    columns = len(data[0])
    print("Number of rows: ", rows)
    print("Number of columns: ", columns)
    print('Titles of table:')
    for title in data[0]:
        print(title, end=', ')
    print('\n')
    return data
