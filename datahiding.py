class HidingDemo:
    "Program for Hiding Data"
    _num = 0
 
    def numbercount(self):
        self._num += 1
        print("Number Count =", self._num)
number=HidingDemo()
number.numbercount()
print(number._num)
   
