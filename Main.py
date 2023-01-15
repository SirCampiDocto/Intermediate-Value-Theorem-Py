# h is the value of the difference of both functions at a given point
def h(x, x1,function1, function2):
    try: 
        return function1(x) - function2(x, x1)
    except TypeError:
        try: return function1(x, x1) - function2(x)
        except TypeError:
            try:
                return function1(x) - function2(x)
            except TypeError: return function1(x) - function2


# function j results as testing how close it is to 0...
# ... the difference between both functions
def j(x1, function1, function2, func1min, func1max):
    minimum = func1min
    maximum = func1max
    mid = (minimum+maximum)/2
    while True:
        if maximum == mid:
            return mid
        elif minimum == mid:
            return mid
        var_h = h(mid,x1,function1, function2)
        #if h(alpha, x1) < 0 and h(beta, x1) > 0:
        if var_h> 0:
            maximum = mid
        elif var_h < 0:
            minimum = mid
        elif var_h == 0:
            return mid
        mid = (minimum+maximum)/2