from .operation import Operation

class Function:
    def __init__(self,
                 func=None,
                 operation=0,
                 left=None,
                 right=None,
                 label=""):
        self.func = func #only for leafs
        self.operation = operation
        self.left = left
        self.right = right
        self.label = label

    def __rmul__(self, other):
        return self.__mul__(other)
    def __mul__(self, other):
        other = Utilities.transformToFunction(other)
        return Function(None, Operation.MLT, self, other)
    def __radd__(self, other):
        return self.__add__(other)
    def __add__(self, other):
        other = Utilities.transformToFunction(other)
        return Function(None, Operation.PLUS, self, other)
    def __rsub__(self, other):
        return other.__sub__(self)
    def __sub__(self, other):
        other = Utilities.transformToFunction(other)
        return Function(None, Operation.MINUS, self, other)
    def __div__(self, other):
        other = Utilities.transformToFunction(other)
        return Function(None, Operation.DIV, self, other)
    def __neg__(self):
        return Function(None, Operation.MLT, Function(func=lambda _:-1), self)
    
    def __call__(self, x):
        if Utilities.isNum(x): 
            return self.__evalRecursive(x, self)
        
        return Function(None, Operation.COMPOSE, self, Utilities.transformToFunction(x))

    def __evalRecursive(self, x, function):
        if function.left == None and function.right == None:
            return self.func(x)
        assert (function.left != None and function.right != None),"Operation tree constructed poorly!"
        return Operation.eval(function, x)

    def __str__(self):
        return f"<Function name='{self.label}', left={self.left}, right={self.right}, op={self.operation}>"
    

import types
class Utilities:
    @staticmethod
    def isNum(x):
        return isinstance(x, int) or isinstance(x, float)
    @staticmethod
    def transformToFunction(x):
        if isinstance(x, Function): return x
        if Utilities.isNum(x):
            return Function(func=lambda _: x)
        if isinstance(x, types.FunctionType):
            return Function(func=x)
        