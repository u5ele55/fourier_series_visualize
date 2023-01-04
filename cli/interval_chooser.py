
class IntervalChooser:
    def __init__(self, length, pointCnt = 100):
        self.length = length
        self.pointCnt = pointCnt
    def choose(self):
        print("Choose interval to display functions on:")
        
        m = {
            1: [self.length * (2*i/self.pointCnt - 1) for i in range(self.pointCnt+1) ],
            2: [self.length * (2*i/self.pointCnt - 3) for i in range(self.pointCnt * 3+1) ],
        }
        
        for key in m:
            l = m[key][0]
            r = m[key][-1]
            print(f"\t{key}.", f'[{l}; {r}]')
            
        choice = int( input("Enter number in list: ") )
        return m[choice]