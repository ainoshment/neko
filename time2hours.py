def time2hours(time):
    """Convert time to hours
    Args:
        time (str): "03:05:21"
    Returns
        hours (int): 3.089166666666667
    """
    if type(time) is not str:
        raise TypeError("a string is required")
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    second = int(time.split(":")[2])
    hours = hour + (minute / 60) + (second / 3600)
    return hours
