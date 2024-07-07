import numpy as np


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
