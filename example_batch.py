"""
Illustrate the usage of paddle.batch
"""
from __future__ import print_function
import paddle.batch as batch

def simple_reader():
    for i in xrange(105):
        yield i

if __name__ == '__main__':
    print("Testing for drop_last=False")
    reader = batch(simple_reader, 10, drop_last=False)
    for i, data in enumerate(reader()):
        print("{}: {}".format(i, data))

    print("Testing for drop_last=True")
    reader = batch(simple_reader, 10, drop_last=True)
    for i, data in enumerate(reader()):
        print("{}: {}".format(i, data))
