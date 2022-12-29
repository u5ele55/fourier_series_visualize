import math
from .function import Function

x = Function(lambda x: x, label = 'x')
cos = Function(math.cos, label = "cos")
sin = Function(math.sin, label = "sin")
sqrt = Function(math.sqrt, label = "sqrt")

def integral(function: Function, a: float, b: float, step = 0.001) -> float:
    assert b > a
    h = step
    cnt = int( (b-a) / h )
    res = 0

    for i in range(cnt):
        res += function(a + (b-a)*((2*i+1)/(2*cnt))) * h
    #if res < 1e-15: res = 0
    return res

def fourier_series_coeff_a(f: Function, n: int):
    if (n == 0): return integral(f, -math.pi, math.pi) / math.pi
    assert n > 0
    return integral( f * cos (n*x), -math.pi, math.pi ) / math.pi

def fourier_series_coeff_b(f: Function, n: int):
    assert n > 0
    return integral( f * sin (n*x), -math.pi, math.pi ) / math.pi

def get_fourier_partial_series(f: Function, N: int):
    assert N >= 0
    func = Function( lambda _: fourier_series_coeff_a(f, 0) / 2 )
    for i in range( 1, N+1 ):
        func = func + fourier_series_coeff_a(f, i) * cos(i * x) + fourier_series_coeff_b(f, i) * sin(i * x)
        
    return func
 