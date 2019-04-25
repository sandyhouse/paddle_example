"""
This file shows the usage of paddle datasets.
"""

import paddle.dataset.cifar as cifar

if __name__ == '__main__':
    print(">>>CIFAR DATA")
    print("\ttrain100")
    for data, label in cifar.train100():
        print("label: {}".format(label))
    print("\ttest100")
    for data, label in cifar.test100():
        print("label: {}".format(label))
    print("\ttrain10")
    for data, label in cifar.train10():
        print("label: {}".format(label))
    print("\ttest10")
    for data, label in cifar.test10():
        print("label: {}".format(label))