"""
Dummy
"""


class Dummy(object):
    """
    Dummy class
    """
    def __init__(self):
        self.some_property = None


if __name__ == '__main__':

    register = {'Dummy': Dummy}

    d = Dummy()

    for k, v in register.items():
        if isinstance(d, v):
            print(k)
            break
    else:
        print('Not registered')
