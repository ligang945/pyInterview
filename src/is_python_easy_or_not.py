class A(object):
    x = 1
    gen = (lambda x: (x for x in range(10)))(x)


if __name__ == "__main__":
    print(A.gen)
