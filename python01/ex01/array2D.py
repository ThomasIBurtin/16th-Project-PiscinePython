import numpy


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list between specified start and end indices.
    Parameters:
        - family (list): A 2D list where each sublist represents a row of data.
        - start (int): The starting index for slicing.
        - end (int): The ending index for slicing.
    Returns:
        - list: A sliced portion of the `family` list as a new 2D list.
    """
    try:
        if not isinstance(family, list) or not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("bad type")
        if not all((len(item) == len(family[0]) for item in family)):
            raise ValueError("all mini_tabs must have same lenght")
        numpy_array = numpy.array(family)
        print(f"My shape is : {numpy_array.shape}")
        print(f"My new shape is : {numpy_array[start:end].shape}")
        return numpy_array[start:end].tolist()

    except Exception as error:
        print(f"{type(error).__name__} : {error}")
