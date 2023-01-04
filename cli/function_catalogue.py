from function.function import Function
from transformation.usual_functions import *

class CLIFunctionCatalogue:
    def requestFunction(self):
        print("You can choose one function from this list:")
        funcs = [ 
            x, x*x, x*sin(x), ln(x*x + x + 2), x + sin(2*x), 
            x+math.acos, sin(x) / x, sin(x*x)
        ]

        ind = 0
        for f in funcs:
            print(f"\t{ind}.", f)
            ind += 1
        choice = int( input(f"Enter your choice [0-{len(funcs)-1}]: ") )
        assert 0 <= choice < len(funcs), "Invalid choice"

        return funcs[choice]