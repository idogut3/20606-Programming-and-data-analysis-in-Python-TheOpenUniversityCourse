import numpy as np

from date import Date


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


def scoping_data(data: np.ndarray, names: list) -> np.ndarray:
    for name in names:  # Lopping through the list of names (That we need to deleter their columns)

        # Finding out the title of each column we want to delete (Might be more
        # than 1 column with the same name we want to delete if someone inserted it incorrectly)
        names_of_titles_of_columns_to_delete = np.where(data[0] == name)

        # Deleting all the columns that we were asked to delete by their title along the y_axis
        y_axis = 1
        data = np.delete(data, names_of_titles_of_columns_to_delete, y_axis)
    return data


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
    data = np.delete(data, np.where(mask == False)[0] + 1, x_axis)
    return data


arr = [
    ['rar', 'Close Approach Date', 'AVIRON'],
    ['rar1', '1995-01-01', 'AVIRON1'],
    ['rar2', '1995-01-01', 'AVIRON2'],
    ['rar3', '1995-01-01', 'AVIRON3'],
    ['rar4', '9999-01-01', 'AVIRON4'],
    ['rar5', '1995-01-01', 'AVIRON5'],
    ['rar6', '1995-01-01', 'AVIRON6'],
    ['rar7', '1995-01-01', 'AVIRON7'],
    ['rar8', '1995-01-01', 'AVIRON8'],
    ['rar9', '1995-01-01', 'AVIRON9'],
    ['rar10', '1995-01-01', 'AVIRON10'],
    ['rar11', '2000-01-01', 'AVIRON11'],
    ['rar12', '2001-01-01', 'AVIRON12'],
    ['rar13', '1995-01-01', 'AVIRON13'],
    ['rar14', '2025-05-01', 'AVIRON14'],
]

arr = np.array(arr)
print(mask_data(arr))
