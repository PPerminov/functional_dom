from quads import *

def dom_unit(name,params,children,content):
    return quad(name,params,children,content)

def get_name(unit):
    return first(unit)

def get_params(unit):
    return second(unit)

def get_children(unit):
    return third(unit)

def get_content(unit):
    return fourth(unit)
