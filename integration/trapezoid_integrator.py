from .integrator import *

class TrapezoidIntegrator(Integrator):
    def integrate(self, func: Function, a: float, b: float) -> float:

        oldVal = func(a)

        steps = int((b-a) / self.step)

        res = 0

        for s in range(steps):
            newVal = func( a + self.step * s )
            res += self.step * (oldVal + newVal) / 2
            oldVal = newVal
        
        #fixing last trapezoid
        newVal = func( b )
        res += ((b-a) - self.step * steps) * self.step * (oldVal + newVal) / 2

        return res