class Operation:
    MLT = 1
    PLUS = 2
    MINUS = 3
    COMPOSE = 4
    DIV = 5

    @staticmethod
    def eval(subFunction, x: float):
        operation = subFunction.operation
        f1 = subFunction.left
        f2 = subFunction.right
        if operation == Operation.MLT:
            return f1(x) * f2(x)
        if operation == Operation.PLUS:
            return f1(x) + f2(x)
        if operation == Operation.MINUS:
            return f1(x) - f2(x)
        if operation == Operation.COMPOSE:
            return f1(f2(x))
        if operation == Operation.DIV:
            return f1(x) / f2(x)
        assert True == False
