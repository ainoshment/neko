def time2minutes(time):
    """Convert time to minutes
    Args:
        time (str): "03:05:21"
    Returns
        minutes (int):185.35
    """
    if type(time) is int:
        raise TypeError("a string is required (got type int)")
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    second = int(time.split(":")[2])
    minutes = (hour * 60) + minute + (second / 60)
    return minutes
