class calculator:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
    def sum(self):
        print(self.number1+self.number2)
    def subtract(self):
        print(self.number1-self.number2)
    def multiply(self):
        print(self.number1*self.number2)
    def divide(self):
        if self.number2 == 0:
            print("Invalid")
        else:
            print(self.number1/self.number2)

result = calculator(3,2)
result.subtract()
