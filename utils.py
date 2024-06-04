import math

def get_radian(degree:float)->float:
    return (math.pi/180)*degree

def get_degree(radian:float)->float:
    return (180*radian)/math.pi

def lin_slope(char_slope:float, path_slope:float)->float:
    arg = (char_slope - path_slope)/(1 + char_slope*path_slope)
    arg = abs(arg)
    return get_degree(math.atan(arg))
