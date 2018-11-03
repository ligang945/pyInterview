def foo(x):
    print("executing foo(%s)" % (x))


class A(object):

    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


foo(0)

a = A()
a.foo(1)
a.class_foo(2)
a.static_foo(3)

A.class_foo(2)
A.static_foo(3)


class Test(object):
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1

if __name__ == '__main__':
    print(Test.num_of_instance)   # 0
    t1 = Test('jack')
    print(Test.num_of_instance)   # 1
    t2 = Test('lucy')
    print(t1.name, t1.num_of_instance)  # jack 2
    print(t2.name, t2.num_of_instance)  # lucy 2


"""
这里p1.name="bbb"是实例调用了类变量,这其实和上面第一个问题一样,就是函数传参的问题,
p1.name一开始是指向的类变量name="aaa",但是在实例的作用域里把类变量的引用改变了,
就变成了一个实例变量,self.name不再引用Person的类变量name了.
"""


class Person:
    name = "aaa"

p1 = Person()
p2 = Person()
p1.name = "bbb"
print(p1.name)  # bbb
print(p2.name)  # aaa
print(Person.name)  # aaa


sub1 = "python string!"
b = "i am a {0}".format(sub1)
print(b)

t = (1, 2, 3)
print("this is %s" % (t,))
