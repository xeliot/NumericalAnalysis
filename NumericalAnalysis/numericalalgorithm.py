import math

def solve(array):
    positive = []
    negative = []
    for i in range(1, len(array)):
        if array[i] > 0:
            positive.append(array[i])
        elif array[i] < 0:
            negative.append(array[i] * -1)
    if array[0] > 0:
        # upperbound: x positive; lowerbound: x negative
        if len(negative) == 0:
            upperbound = 1
            lowerbound = max(positive) * len(positive) * -1
        elif len(positive) == 0:
            upperbound = max(negative) * len(negative)
            lowerbound = -1
        else:
            upperbound = max(negative) * len(negative)
            lowerbound = max(positive) * len(positive) * -1
    else:
        # upperbound: x negative; lowerbound: x positive
        if len(negative) == 0:
            upperbound = max(positive) * len(positive)
            lowerbound = -1
        elif len(positive) == 0:
            upperbound = 1
            lowerbound = max(negative) * len(negative) * -1
        else:
            lowerbound = max(negative) * len(negative) * -1
            upperbound = max(positive) * len(positive)
    marker = lowerbound
    print lowerbound
    print upperbound
    count = 0
    while(True):
        count += 1
        #print lowerbound
        #print upperbound
        value = 0
        for i in range(0, len(array)):
            value += array[len(array)-i-1]*(marker**i)
        if (abs(value-0) < 0.00000001):
            print count
            return marker
        if ((value < 0) and (array[0]>0)) or ((value > 0) and (array[0]<0)):
            lowerbound = marker
            marker = marker+((upperbound-marker)/2.0)
        else:
            upperbound = marker
            marker = marker-((marker-lowerbound)/2.0)
    #return marker
        
def recurse(lowerbound, upperbound, marker, function):
    value = 0
    for i in range(0, len(function)):
        value += function[len(function)-i-1]*(marker**i)
    if (abs(value-0) < 0.001):
        return marker
    if (value < 0):
        return recurse(marker, upperbound, marker+((upperbound-marker)/2.0), function)
    else:
        return recurse(lowerbound, marker, marker-((marker-lowerbound)/2.0), function)    
    

def function1(num):
    return math.e**(num-3)

def function2(num):
    return num * math.log(num)

def combined_function(num):
    return function1(num) - function2(num)

def slope(function, x):
    dx = 0.00001
    '''
    value1 = 0
    value2 = 0
    for i in range(0, len(function)):
        value1 += function[len(function)-i-1]*((x-dx)**i)
        value2 += function[len(function)-i-1]*((x+dx)**i)
    '''
    value1 = function(x-dx)
    value2 = function(x+dx)
    previous = (value2-value1)/(2*dx)
    dx = dx/2.0
    '''
    value1 = 0
    value2 = 0
    for i in range(0, len(function)):
        value1 += function[len(function)-i-1]*((x-dx)**i)
        value2 += function[len(function)-i-1]*((x+dx)**i)
    '''
    value1 = function(x-dx)
    value2 = function(x+dx)
    current = (value2-value1)/(2*dx)
    while(True):
        '''
        value1 = 0
        value2 = 0
        for i in range(0, len(function)):
            value1 += function[len(function)-i-1]*((x-dx)**i)
            value2 += function[len(function)-i-1]*((x+dx)**i)
        '''
        value1 = function(x-dx)
        value2 = function(x+dx)
        current = (value2-value1)/(2*dx)
        if(abs(math.atan(previous)-math.atan(current))<0.00000001):
            return current
        previous = current
        dx = dx/2.0
        
'''
array = [3, 0, -14, 0, 0, 13, 0, -14]
#array = [2, 3, 4, 5]
print solve(array)
'''

def integration(function, x1, x2):
    previousdx = (x2-x1)/10.0
    currentdx = previousdx/2.0
    while(abs((function(currentdx)*currentdx)-(function(previousdx)*previousdx)) > 0.000001):
        previousdx = currentdx
        currentdx = currentdx/2.0
    marker = x1
    area = 0
    while(marker < x2):
        area += function(marker)*currentdx
        marker += currentdx
    return area
    
def newtons(function):
    previous = 1.11111
    current = previous - (function(previous)/slope(function, previous))
    while(abs(current - previous) > 0.000001):
        previous = current
        current = current - (function(current)/slope(function, current))
    return current

def minimum(function):
    previous = 3.11111
    a = (slope(function, previous) - slope(function, previous-0.000000001))/0.000000001
    current = previous - (slope(function, previous)/a)
    while(abs(current - previous) > 0.000001):
        previous = current
        a = (slope(function, previous) - slope(function, previous-0.000000001))/0.000000001
        current = current - (slope(function, previous)/a)
    return current

def gradient(function):
    lr = 0.1
    x = 0
    count = 0
    while(abs(slope(function, x)) > 0.000000001):
        x -= lr*slope(function, x)
        count += 1
    print count
    return x

def solve_system(function):
    return newtons(function)

def area(function1, function2, x1, x2):
    return abs(integration(function1, x1, x2) - integration(function2, x1, x2))

print solve_system(combined_function)
print area(function1, function2, 2, 4)
