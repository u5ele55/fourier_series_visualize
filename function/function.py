class Operation:
    MLT = 1
    PLUS = 2
    MINUS = 3
    COMPOSE = 4
    DIV = 5
    POWER = 6

    @staticmethod
    def eval(subFunction, x: float):
        operation = subFunction.operation
        f1 = subFunction.left
        f2 = subFunction.right
        m = {
            Operation.MLT: lambda g,h: g(x) * h(x),
            Operation.PLUS: lambda g,h: g(x) + h(x),
            Operation.MINUS: lambda g,h: g(x) - h(x),
            Operation.COMPOSE: lambda g,h: g(h(x)),
            Operation.DIV: lambda g,h: g(x) / h(x),
            Operation.POWER: lambda g,h: g(x) ** h(x),
        }
        assert operation in m.keys(), "Invalid operation"
        return m[operation](f1, f2)
    
    @staticmethod
    def symbol(operation):
        m = {
            Operation.MLT: '*',
            Operation.PLUS: ' + ',
            Operation.MINUS: ' - ',
            Operation.COMPOSE: '(',
            Operation.DIV: ' / ',
            Operation.POWER: ' ** '
        }
        assert operation in m.keys(), "Invalid operation"
        return m[operation]
        

class Function:
    def __init__(self,
                 func = None,
                 operation = 0,
                 left = None,
                 right = None,
                 label = ""):
        self.func = func #only for leafs
        self.operation = operation
        self.left = left
        self.right = right
        
        self.label = label

    def real(self):
        return Function(lambda t: self(t).real, label = f'Re(self.label)' if self.label else self.label)
    def imag(self):
        return Function(lambda t: self(t).imag, label = f'Im(self.label)' if self.label else self.label)

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
    def __rpow__(self, other):
        other = Utilities.transformToFunction(other)
        return Function(None, Operation.POWER, other, self)
    def __pow__(self, other):
        other = Utilities.transformToFunction(other)
        return Function(None, Operation.POWER, self, other)
    def __rtruediv__(self, other):
        other = Utilities.transformToFunction(other)
        return other.__truediv__(self)
    def __truediv__(self, other):
        other = Utilities.transformToFunction(other)
        return Function(None, Operation.DIV, self, other)
    def __neg__(self):
        return Function(None, Operation.MLT, Function(func=lambda _:-1, label="-1"), self)
    
    def __call__(self, x):
        if Utilities.isNum(x): 
            return self.__evalRecursive(x, self)
        
        return Function(None, Operation.COMPOSE, self, Utilities.transformToFunction(x))

    def __evalRecursive(self, x, function):
        if function.left == None and function.right == None:
            return self.func(x)
        assert (function.left != None and function.right != None), "Operation tree constructed poorly!"
        return Operation.eval(function, x)

    def __str__(self):
        return Function.__toStr(self)

    @staticmethod
    def __toStr(node):
        collectedStr = '' 
        if node.left == None and node.right == None:
            return node.label
        
        if node.left: 
            collectedStr += Function.__toStr(node.left)
        collectedStr += Operation.symbol(node.operation)
        if node.right: 
            collectedStr += Function.__toStr(node.right)
        
        if node.operation is Operation.COMPOSE: 
            collectedStr += ')'
        return collectedStr

    

import types
class Utilities:
    @staticmethod
    def isNum(x):
        return isinstance(x, int) or isinstance(x, float)
    @staticmethod
    def transformToFunction(x):
        if isinstance(x, Function): return x
        if Utilities.isNum(x):
            return Function(func=lambda _: x, label=str(x))
        if isinstance(x, types.FunctionType): 
            genLabel = ""
            return Function(func=x, label=genLabel)
        if '<built-in function' in str(x):
            genLabel = str(x).replace('<built-in function ', '')[:-1]
            return Function(func=x, label=genLabel)
        