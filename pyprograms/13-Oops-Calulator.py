class Calculator():
    #Properties/ member variables
    num1=0
    num2=0
    result = 0

    #method
    def add(self,firstnum,secondnum):
        self.num1 = firstnum
        self.num2= secondnum
        self.result = self.num1 +self.num2
        return self.result

    def subtract(self, firstnum, secondnum):
        self.num1 = firstnum
        self.num2 = secondnum
        self.result = self.num1 - self.num2
        return self.result

    def multiply(self, firstnum, secondnum):
        self.num1 = firstnum
        self.num2 = secondnum
        self.result = self.num1 * self.num2
        return self.result

    def info(self):
        print("first number is ",self.num1)
        print("second number is ", self.num2)


#myCalculator1 object
myCalculator1 = Calculator()
result = myCalculator1.add(10,20)
myCalculator1.info()
print("result of addition ",result)

result = myCalculator1.multiply(2,20)
print("result of multiplication ",result)
