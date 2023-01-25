from .usual_functions import *
from integration.integrator import Integrator

class FourierTransformation:
    def __init__(self, l: float, integrator: Integrator):
        '''
        l - right border of interval on which fourier series takes place in (interval [-l; l])
        '''
        self.l = l
        self.coeffs_a = {} 
        self.coeffs_b = {}
        self.integrator = integrator
    
    def fourier_series_coeff_a(self, f: Function, n: int) -> float: 
        assert n >= 0
        if (n in self.coeffs_a):
            return self.coeffs_a[n]
        if (n == 0): 
            self.coeffs_a[n] = self.integrator.integrate( f, -self.l, self.l ) / self.l
        else:
            self.coeffs_a[n] = self.integrator.integrate( f * cos (x * (n * math.pi / self.l)), -self.l, self.l ) / self.l
        
        return self.coeffs_a[n]
    
    def fourier_series_coeff_b(self, f: Function, n: int) -> float:
        assert n > 0
        if (n not in self.coeffs_b): 
            self.coeffs_b[n] = self.integrator.integrate( f * sin (x * (n * math.pi / self.l)), -self.l, self.l ) / self.l
        
        return self.coeffs_b[n]
    
    def get_fourier_partial_series(self, f: Function, N: int) -> Function:
        assert N >= 0
        func = Function( lambda _: self.fourier_series_coeff_a(f, 0) / 2 )
        for i in range( 1, N+1 ):
            func = func + self.fourier_series_coeff_a(f, i) * cos(x * (i * math.pi / self.l)) \
                        + self.fourier_series_coeff_b(f, i) * sin(x * (i * math.pi / self.l))
        
        return func
    