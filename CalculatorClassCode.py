class Calculator():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        print(self.num1+self.num2)
    def subtract(self):
        print(self.num1-self.num2)
    def mutiply(self):
        print(self.num1*self.num2)
    def divide(self):
        try:
            print(self.num1/self.num2)
        except ZeroDivisionError:
            print('Both your numbers are zero. Please change them.')
            
cal = Calculator(6,5)

cal.add()
cal.subtract()
cal.mutiply()
cal.divide()