def compound_interest(principal, rate, time, n):
    """
    Calculate the compound interest.

    :param principal: Initial amount of money
    :param rate: Annual interest rate (in decimal)
    :param time: Time the money is invested for (in years)
    :param n: Number of times interest is compounded per year
    :return: Compound interest
    """
    return principal * (1 + rate / n) ** (n * time)
print(compound_interest(1000, 0.05, 10, 4))  # Example usage