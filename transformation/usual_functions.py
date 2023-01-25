from function.function import Function
import math

x = Function(lambda x: x, label = 'x')
cos = Function(math.cos, label = "cos")
sin = Function(math.sin, label = "sin")
sqrt = Function(math.sqrt, label = "sqrt")
ln = Function(math.log, label = "ln")
abs = Function(math.fabs, label = "abs")