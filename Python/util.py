"""
some utility for algorithms practice
"""
# just set the right function in production
from typing import Any, List

log = print


def print_matrix(matrix):
    for i in range(len(matrix)):
        log(matrix[i])


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def creat_linked_list_from_array(array: List[Any]) -> ListNode:
    if len(array) == 0:
        return None
    current = ListNode(array[0])
    head = current
    for element in array[1:]:
        current.next = ListNode(element)
        current = current.next
    return head


def show_linked_list(head: ListNode):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    log("->".join(str(x) for x in result))


def equal(reality, expect):
    if expect == reality:
        log("Success,passed test with output:{reality}".format(
            reality=reality))
    else:
        log("Falil,expect:{expect} but get:{reality}".format(expect=expect,
                                                             reality=reality))


def same_elements(reality: List[Any], expect: List[Any]):
    if len(expect) == 0:
        if len(reality) == 0:
            return log("Success,passed test with output:{reality}".format(
                reality=reality))
        else:
            return log("Falil,expect:{expect} but get:{reality}".format(
                expect=expect, reality=reality))

    if len(reality) == 0:
        return log("Falil,expect:{expect} but get:{reality}".format(
            expect=expect, reality=reality))

    if type(expect[0]) == list:
        expect = sorted(expect)
        reality = sorted(reality)
        return equal(expect, reality)

    if set(expect) == set(reality):
        log("Success,passed test with output:{reality}".format(
            reality=reality))
    else:
        log("Falil,expect:{expect} but get:{reality}".format(expect=expect,
                                                             reality=reality))


class Test(object):
    def __init__(self, method):
        self.method = method
        log("test start")

    def equal(self, expect, *args):
        equal(self.method(*args), expect)

    def same_elements(self, expect, *args):
        same_elements(self.method(*args), expect)


if __name__ == "__main__":
    # test for test :)

    # Linked List related test
    origin = creat_linked_list_from_array([3, 2, 1, 4, 5])
    show_linked_list(origin)

    class foo:
        def fooPlusTwo(a, b):
            return a + b + 1

        def fooPlusOne(a):
            return a + 1

        def reverse(array: List[Any]):
            return array[::-1]

    f = foo()
    t1 = Test(foo.fooPlusTwo)
    t1.equal(4, 1, 2)

    t2 = Test(foo.fooPlusOne)
    t2.equal(4, 1)

    t3 = Test(foo.reverse)
    t3.same_elements([1, 2, 3, 4], [3, 2, 1])
    t3.same_elements([1, 2, 3], [3, 2, 1])
    t3.equal([1, 2, 3], [3, 2, 1])
    t3.same_elements([[1], [2], [3]], [[3], [2], [1]])
