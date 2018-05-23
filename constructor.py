from unit import dom_unit, get_name, get_params, get_content, get_children
from re import compile, IGNORECASE

def filer(x):
    return open(x,'r')

def reader(x):
    yield x.readline()

def matcher(str,expr='\s'):
    return True if compile(expr).match(str) else False


def xml_to_array(x):
    def new_liner(xml):

    def de_spacer(y):
        out=[]
        counter = 0
        while True:
            if counter == len(y) - 1:
                break
            if y[counter] == "\n" or y[counter] == "\r\n":
                counter+=1
                while True:
                    if not matcher(y[counter]):
                        break
                    counter+=1
                continue
            out.append(y[counter])
            counter += 1
        return out
    flat_xml=list(x.read())
    return ''.join(de_spacer(flat_xml))




print(xml_to_array(filer('test.xml')))


def parse_tag(x):
    if






"""name_begins_with=['<', not compile('\S')]
name_ends_with=[' ']
tag_begins_with=['<']
params_key_begins_with=[' ']
params_key_ends_with=['=']
params_value_begins_with=['="']
params_value_ends_with=['"']
tag_ends_with=['>']
tag_closes_with=['</','/>']

veryfirst starts with <?
open tag begins with < without /
if opening tag ends with /> - tag is closed
closing tag begins with </ and ends with >
parameters begins after name. separating with spaces

children begins when tag not closed and next tag opens
data begins when tag not closed till first <"""
