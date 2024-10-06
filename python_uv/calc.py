def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
    ----
        a (int): First number.
        b (int): Second number.

    Raises:
    ------
        TypeError: Both a and b must be integers.

    Returns:
    -------
        int: sum of a and b.

    """
    if not isinstance(a, int) or not isinstance(b, int):
        err_msg = "Both a and b must be integers."
        raise TypeError(err_msg)
    return a + b
