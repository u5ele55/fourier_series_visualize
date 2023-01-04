import matplotlib.pyplot as plt

class PlotCreator:
    def __init__(self, initialFunc, drawPoints):
        self.draw_interval = drawPoints
        self.initialFunc = initialFunc

    def showPlot(self, fourierFunc):
        plt.plot(self.draw_interval, [self.initialFunc(k) for k in self.draw_interval])
        plt.plot(self.draw_interval, [fourierFunc(k) for k in self.draw_interval])
        plt.show()