class X(object):

    def __init__(self, a, b):
        self.m = a
        self.n = b
        print('__init__ with a:{}, b:{}'.format(a, b))

    def __call__(self, a, b):
        self.m = a
        self.n = b
        print('__call__ with a:{}, b:{}'.format(a, b))

    def __del__(self):
        del self.m
        del self.n

xInstance = X(1, 2)

xInstance(3, 4)
print(xInstance.m)
print(xInstance.n)

print(callable(xInstance))
