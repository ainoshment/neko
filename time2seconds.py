def time2seconds(time):
    """Convert time to seconds
    Args:
        time (str): "03:05:11"
    Returns
        minutes (int):11111
    """
    if type(time) is int:
        raise TypeError("a string is required (got type int)")
    unit = [3600, 60, 1]
    seconds = sum(int(x) * int(y) for (x, y) in zip(unit, time.split(":")))
    return seconds
