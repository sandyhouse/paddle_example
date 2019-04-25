"""
This file shows the usage of paddle datasets.
"""

import paddle.dataset.cifar as cifar

if __name__ == '__main__':
    print(">>>CIFAR DATA")
    print("\ttrain100")
    datasets = cifar.train100()
    for data, label in datasets():
        print("label: {}".format(label))