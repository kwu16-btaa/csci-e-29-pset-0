#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    last8 = 0
    try:
        last8 = int(str(some_int)[-8:])
    except ValueError:
        print("That was not a valid number")

    return last8


def optimized_fibonacci(f):
    """ Return fibonacci sequence number at position f
    :param f: int
    :return: int of fibonacci sequence at position
    """

    if f <= 1:
        return f

    prev, curr = 0, 1
    for i in range(1, f):
        prev, curr = curr, curr + prev

    return curr


class SummableSequence(object):
    """ Class that implements a summable function which generalizes the fibonacci code implementation
    The class creates an instance giving initial of arbitrary length fibonacci sequence
    that contains a function which returns sequence value at the ith position

    """

    init_seq = []

    def __init__(self, *initial):
        self.init_seq = list(initial)
        self.seq_len = len(self.init_seq)

    def __call__(self, i):

        if i < self.seq_len - 1:
            return self.init_seq[i]

        for k in range(self.seq_len-1, i):
            self.init_seq, self.init_seq[self.seq_len - 1] = self.init_seq[1:] + \
                self.init_seq[:1], sum(self.init_seq)

        return self.init_seq[self.seq_len - 1]

if __name__ == "__main__":

    print("f(1000000)[-8:]", last_8(optimized_fibonacci(1000000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(1000000)[-8:]:", last_8(new_seq(1000000)))
