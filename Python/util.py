"""
some utility for algorithms practice
"""
# just set the right function in production
log = print


def equal(reality, expect):
    if expect == reality:
        log('Success,passed test with output:{reality}'.format(
            reality=reality))
    else:
        log('Falil,expect:{expect} but get:{reality}'.format(
            expect=expect,
            reality=reality
        ))


class Test(object):
    def __init__(self, method):
        self.method = method
        log('test start')

    def equal(self, expect, *args):
        equal(self.method(*args), expect)


if __name__ == '__main__':
    # test for test :)
    class foo:
        def fooPlusTwo(a, b):
            return a + b + 1

        def fooPlusOne(a):
            return a + 1

    f = foo()
    t1 = Test(foo.fooPlusTwo)
    t1.equal(4, 1, 2)

    t2 = Test(foo.fooPlusOne)
    t2.equal(4, 1)
