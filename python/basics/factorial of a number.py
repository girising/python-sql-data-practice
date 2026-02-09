def calculate_factorial(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Write your code here.
    a = 1
    for i in range(1, n + 1):
        a *= i

    return a
