def compound_interest(principal, rate, time):
    """
    Args:
     principal(float)
     rate(float)
     time(int32)
    Returns:
     float
    """
    # Write your code here.
    a = 0.0
    a = principal * ((1 + rate / 100) ** time)
    ci = a - principal

    return ci
