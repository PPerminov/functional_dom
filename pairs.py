def cons(car, cdr):
    return lambda job_type: car if job_type == 'car' else cdr if job_type == 'cdr' else False


def car(cons_sample):
    return cons_sample('car')


def cdr(cons_sample):
    return cons_sample('cdr')
