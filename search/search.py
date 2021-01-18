
#Golden-section search to find the extreme of the function in the given interval
#Input Parameters:
#func - the function of interest. Must be of the type float -> float
#lo,hi: float/int. low and high intervals for the x values. the extreme value must be strictly within ]lo.hi[
#xtol: float/int. the maximum length of interval for the return value
#mode: string.
#      max -> default. finds the maximum value in the given interval
#      min -> finds the minimum value in the given interval
#Returns:
#x_lo,x_hi: floats. the x interval at which extreme value occurs in the given interval of the given function.
def golden_section_search(func,lo,hi,xtol,mode='max'):
    phi = (1+5**0.5)/2
    def get_lo_interval(lo,hi):
        c1 = lo + (hi-lo)/(2+2*phi)
        return c1
    def get_hi_interval(lo,hi):
        c2 = hi - (hi-lo)/(2+2*phi)
        return c2
    def applyfunc(xcur):
        ycur = func(xcur)
        if mode=='min':
            ycur *= -1
        return ycur

    c1,c2 = get_lo_interval(lo,hi),get_hi_interval(lo,hi)
    fc1,fc2 = applyfunc(c1),applyfunc(c2)

    while (hi-lo)>xtol:
        if fc1>fc2:
            hi = c2
            c2 = get_hi_interval(lo,hi)
            fc2 = applyfunc(c2)
        else:
            lo = c1
            c1 = get_lo_interval(lo,hi)
            fc1 = applyfunc(c1)
    return lo,hi
