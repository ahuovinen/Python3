class calculator:
    def __init__(self) -> None: # basic init method.
        self.res()              # call reset total method.
    def add(self, x):           # addition method
        self.Total += x
    def sub(self, x):           # subtracktion method
        self.Total -= x
    def div(self, x):           # division method
        if x == 0:              # cant divide by zero
            print("dumbass")
        else:
            self.Total /= x
    def mul(self, x):           # multiplication method
        self.Total *= x
    def res(self):              # reset calculator to 0.0
        total = 0.0 
    def getTotal(self):         # return calculator value
        return self.Total
     
def main():
    print("calculator class definition")

if __name__ == "__main__":
    main()
