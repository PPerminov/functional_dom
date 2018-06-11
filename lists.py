from pairs import car, cdr, cons


def special_list(*params, ty=0):
    def worker(parameters):
        if len(parameters) == 1:
            return cons(parameters[0], None)
        return cons(parameters[0], worker(parameters[1::]))
    if ty == 0:
        return worker([i for i in params])
    return worker([i for i in params[0]])


def get_position(list_1, position):
    if not list_1:
        return False
    return head(list_1) if position == 0 else get_position(
        tail(list_1),
        position - 1)


def head(list1):
    return car(list1)


def tail(list1):
    return cdr(list1)


def is_equal_lists(l1, l2):
    if l1 is None and l2 is None:
        return True
    if callable(head(l1)) and callable(head(l2)):
        if not is_equal_lists(head(l1), head(l2)):
            return False
    elif head(l1) != head(l2):
        return False
    return is_equal_lists(tail(l1), tail(l2))
