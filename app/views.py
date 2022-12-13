from django.shortcuts import render

# Create your views here.


# Define function to integrate
def f(x):
    return 1 / (1 + x ** 2)


# Implementing trapezoidal method
def trapezoidal(a, b, n):
    # calculating step size
    h = (b - a) / n

    # Finding sum
    integration = f(a) + f(b)

    for i in range(1, n):
        k = a + i * h
        integration = integration + 2 * f(k)

    # Finding final integration value
    integration = integration * h / 2

    return integration


def home(request):
    result = None
    if request.method == "POST":
        # Input section
        lower_limit = request.POST.get("lower_limit")
        upper_limit = request.POST.get("upper_limit")
        sub_interval = request.POST.get("sub_interval")

        # Call trapezoidal() method and get result
        result = trapezoidal(
            float(lower_limit),
            float(upper_limit),
            int(sub_interval)
        )
        result = round(result,6)

    context = {
        "result":result
    }
    return render(request,'home.html',context)