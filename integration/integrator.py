
from function.function import Function

class Integrator:
    def __init__(self, step: float = 1e-3):
        self.step = step

    def integrate(self, func: Function, a: float, b: float) -> float:
        pass