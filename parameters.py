from pairs import car, cdr, cons
from lists import special_list, head, tail, is_equal_lists


def parameter(key, value):
    return False if key is None or key == '' or value is None or value == '' else cons(key, value)


def get_key(parameter):
    return car(parameter)


def get_value(parameter):
    return cdr(parameter)


def get_value_by_key(parameter, key):
    return cdr(parameter) if car(parameter) == key else False


def parameter_to_string(parameter):
    return ' ' + get_key(parameter) + '="' + get_value(parameter) + '"'


def parameters_to_string(params_list):
    if params_list is None:
        return ''
    return parameter_to_string(head(params_list)) + params_to_string(tail(params_list))


def create_parameters_list(*parameters):
    return special_list(parameters, 1)
