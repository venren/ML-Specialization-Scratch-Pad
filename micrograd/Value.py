class Value:

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"Value(data={self.data:})"
    
    def __add__(self, other):
        return Value(self.data + other.data)
    
    def __mul__(self, other):
        return Value(self.data * other.data)


a= Value(3.0)
b= Value(2.0)
c = Value(4.0)
print(a+b*c)