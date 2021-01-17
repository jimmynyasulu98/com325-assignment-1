class Test:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.radius * 3.14
    def number(self,number):
        return number

if __name__ == "__main__":
    c = Test(3)
    print(c.area())
    print(c.number(4))

