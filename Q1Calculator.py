class Calculator:
    answer = 0
    def clear(self):
        self.answer = 0
    
    def adder(self, input1, input2):
        self.answer = input1+input2
        print("Sum: ",self.answer)

    def subtractor(self, input1, input2):
        self.answer = input1-input2
        print("Subtraction: ",self.answer)

    def multiplier(self, input1, input2):
        self.answer = input1 * input2
        print("Product: ",self.answer)
    
    def divider(self, input1, input2):
        self.answer = input1 / input2
        print("Quotient: ",self.answer)
    
myCalc = Calculator()
input1 = int(input("Enter the 1st number: "))
input2 = int(input("Enter the 2nd number: "))
myCalc.adder(input1,input2)
myCalc.subtractor(input1,input2)
myCalc.multiplier(input1,input2)
myCalc.divider(input1,input2)
myCalc.clear()
print("After clearing: answer = ", myCalc.answer)