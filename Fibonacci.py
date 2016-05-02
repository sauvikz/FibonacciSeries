class Fibonacci(object):
    
    def __init__(self, range_fibonacci):
        self.range_fibonacci = range_fibonacci
        
    def fibonacci_function(self):
        range_of_series = self.range_fibonacci
        range_of_series = range_of_series - 2
        a = 0
        b = 1
        c = 0
        k = 1
        print a,b,
        while k <= range_of_series:
            c = a + b
            k = k + 1
            print c,
            a = b
            b = c
            
print "Welcome to the Fibonacci Series generation."
range_of_fibonacci_series = int(raw_input("How many numbers do you want the series to generate? "))
print "So you want %s numbers to be generated? COOL " % range_of_fibonacci_series
instance = Fibonacci(range_of_fibonacci_series)
instance.fibonacci_function()
        
