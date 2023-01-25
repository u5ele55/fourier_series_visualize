import matplotlib.pyplot as plt

class PlotCreator:
    def __init__(self, initialFunc, drawPoints):
        self.draw_interval = drawPoints
        self.initialFunc = initialFunc
        self.functions = []

    def addFunction(self, func, label: str):
        self.functions.append([func, label])

    def showPlot(self, showAll = True):
        plt.plot(self.draw_interval, [self.initialFunc(k) for k in self.draw_interval], label="f(x)")
        if showAll:
            for f, label in self.functions:
                plt.plot(self.draw_interval, [f(k) for k in self.draw_interval], label=label)
        else:
            plt.plot(self.draw_interval, [self.functions[-1](k) for k in self.draw_interval], label=label)
        plt.legend()
        plt.show()