def convert(feet, inches):
    """
    Convert feet and inches to meters.

    Args:
        feet (float): The number of feet to convert.
        inches (float): The number of inches to convert.

    Returns:
        float: The equivalent distance in meters.
    """
    meters = feet * 0.3048 + inches * 0.0254
    return meters