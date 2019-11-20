from datetime import time


def seconds2time(seconds):
    """
    :type seconds: int
    :param seconds: 11111
    :rtype: str,
    :return: "03:05:11"
    """
    if type(seconds) is str:
        raise TypeError("an integer is required (got type str)")
    if seconds > 86400 or seconds < 0:
        raise ValueError("seconds must be int and in 0..86400")
    hour, minute, second = seconds // 3600, (seconds % 3600) // 60, seconds % 60
    return str(time(hour=hour, minute=minute, second=second))
