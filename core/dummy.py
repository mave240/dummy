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

    register = {
        'String': str,
        'Dummy': Dummy
    }

    d = Dummy()

    # Find the registered type
    for k, v in register.items():
        if isinstance(d, v):
            print(k)
            break
    else:
        print('Not registered')
