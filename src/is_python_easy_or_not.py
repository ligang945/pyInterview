# 1
class A(object):
    x = 1
    gen = (lambda x: (x for x in range(10)))(x)


if __name__ == "__main__":
    print(list(A.gen))


# 2
print('-' * 20)

import time


class Timeit(object):

    def __init__(self, func):
        self._wrapped = func

    def __call__(self, *args, **kws):
        start_time = time.time()
        result = self._wrapped(*args, **kws)
        print("elapsed time is %s " % (time.time() - start_time))
        return result

    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self.__call__(instance, *args, **kwargs)


class A(object):

    @Timeit
    def func(self):
        time.sleep(1)
        print('invoking method func')

a = A()
a.func()

