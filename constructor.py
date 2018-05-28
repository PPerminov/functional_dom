from unit import dom_unit, get_name, get_params, get_content, get_children
from re import compile, IGNORECASE

def filer(x):
    return open(x,'r')

def reader(x):
    yield x.readline()

def matcher(str,expr='\s'):
    return True if compile(expr).match(str) else False

def get_word(text,start_position,end_position=None):
    if matcher(text[start_position]):
        return end_position
    return get_word(text,start_position+1,start_position)


def new_liner(xml):
    out=''
    for pos in range(0,len(xml)):
        if xml[pos] == '<' and out[(len(out) - 1) if len(out) > 0 else 0] != "\n":
            out+="\n"+xml[pos]
        elif xml[pos] =='>':
            out+=xml[pos]+"\n"
        else:
            out+=xml[pos]
    return out





def xml_to_array(x):
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




# print(xml_to_array(filer('test.xml')))
#
#
# def parse_tag(x):
#     if






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

# Get all tags
# (<![^\W].*?>)|(<[^\W].*?>)|(<\/.*?>)|([\w\s]*)

# Get name from tag
# <([\/]?[\w:]+\s+).*?>

# Get all parameters
# <[\/]?[\w:]+\s+(.*?)>

# get keys/values
# ([\w:]*?)="(.*?)"|([\w:]*?)=(\S*)|\s([\w\:\-]+?)\s
