class TestRepr(object):
    def __init__(self, d):
        self.data = d
    def __repr__(self):
        return 'TestRepr(%s)' % self.data
    def __str__(self):
        return '[Value: %s]' % self.data
t = TestRepr(1)
print(t)
t
