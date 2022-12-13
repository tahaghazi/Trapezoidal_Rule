# Trapezoidal Method

# Define function to integrate
def f(x):
    return 1 / (1 + x ** 2)


# Implementing trapezoidal method
def trapezoidal(a, b, n):
    """
    a ----> lower limit of integration
    b ----> upper limit of integration
    n ----> number of sub intervals
    """

    # calculating step size
    h = (b - a) / n

    # Finding sum
    fa_and_fb = (f(a) + f(b)) / 2

    sigma_fk = 0
    # f(a+1*h) + f(a+2*h) +f(a+3*h) +...
    for i in range(1, n):
        fk = f(a + i * h)
        sigma_fk +=  fk

    # Finding final integration value
    result = h * (fa_and_fb + sigma_fk )

    return result


# Input section
a = float(input("Enter lower limit of integration: "))
b = float(input("Enter upper limit of integration: "))
n = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
integration = trapezoidal(a, b, n)

# Print result
print("Integration result by Trapezoidal method is: " , integration)

# Close console
input("Press any key to close")

