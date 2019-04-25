"""
This file shows the usage of paddle datasets.
"""

import paddle.dataset.cifar as cifar

if __name__ == '__main__':
    print(">>>CIFAR DATA")
    print("\ttrain100")
    datas, labels = cifar.train100()
    print("label: {}".format(labels))