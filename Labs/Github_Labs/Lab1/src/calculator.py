def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int | float): First number
        y (int | float): Second number
    Returns:
        int | float: Sum of x and y
    Raises:
        ValueError: If inputs are not numeric
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return x + y


def fun2(x, y):
    """
    Subtracts y from x.
    Args:
        x (int | float): First number
        y (int | float): Second number
    Returns:
        int | float: Difference of x and y
    Raises:
        ValueError: If inputs are not numeric
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return x - y


def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int | float): First number
        y (int | float): Second number
    Returns:
        int | float: Product of x and y
    Raises:
        ValueError: If inputs are not numeric
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return x * y


def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int | float): First number
        y (int | float): Second number
        z (int | float): Third number
    Returns:
        int | float: Sum of x, y, and z
    Raises:
        ValueError: If inputs are not numeric
    """
    if not all(isinstance(val, (int, float)) for val in (x, y, z)):
        raise ValueError("All inputs must be numbers")
    return x + y + z
