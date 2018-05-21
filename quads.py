def quad(first, second, third, fourth):
    def worker(position):
        if position == 'first':
            return first
        elif position == 'second':
            return second
        elif position == 'third':
            return third
        elif position == 'fourth':
            return fourth
        else:
            return False
    return worker


def first(quad_sample):
    return quad_sample('first')


def second(quad_sample):
    return quad_sample('second')


def third(quad_sample):
    return quad_sample('third')


def fourth(quad_sample):
    return quad_sample('fourth')
