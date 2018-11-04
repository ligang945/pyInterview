def login():
    print('in login')


def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator  # function as return value

debug_login = printdebug(login)  # function assign to variable

debug_login()  # execute the returned function


print('-' * 20)


def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator


@printdebug  # combine the printdebug and login
def login():
    print('in login')

login()  # make the calling point more intuitive




class Counter:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@Counter
def foo():
    pass

for i in range(10):
    foo()

print(foo.count)  # 10
