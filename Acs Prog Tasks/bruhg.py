class PassByReference:
    def __init__(self):
        self.variable = 'Original'
        self.change(self.variable)
        print(self.variable)

    def change(self, var):
        var = 'Changed'

def proc1 (x, y):
    x = x - 2
    y = 0

m = 8
n = 10

proc1(m, n)
print(m, n)
