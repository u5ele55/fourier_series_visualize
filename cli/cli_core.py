from .function_catalogue import CLIFunctionCatalogue
from .plot_creator import PlotCreator
from .interval_chooser import IntervalChooser

from function.function import *
from transformation.transformation import *
from integration.trapezoid_integrator import TrapezoidIntegrator

class CLICore:

    def start(self):

        catalogue = CLIFunctionCatalogue()
        func = catalogue.requestFunction()
        length = float( input("Enter length (enter non-positive value to choose Pi): ") )
        if length <= 0: length = math.pi
        intervalChooser = IntervalChooser(length, int(length * 40))
        points = intervalChooser.choose()
        plotCreator = PlotCreator(func, points)
        transformator = FourierTransformation(length, TrapezoidIntegrator())

        N = 0

        while True:
            try: N = int( input("Enter N: ") )
            except: N = -1
            if N < 0: break

            print("\tCalculating partial fourier sum...")
            part_sum = transformator.get_fourier_partial_series(func, N)
            
            print("\tDrawing plot...")
            plotCreator.addFunction(part_sum, f"N = {N}")
            plotCreator.showPlot()  

        print("Terminating...")
