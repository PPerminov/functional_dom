import re
from sys import exit

with open('test.xml', 'r') as htt:
    data = htt.read()


def de_shitter(raw):
    spaces = re.compile('[^\t^\r^\n]+')
    return ''.join(re.findall(spaces, raw))


def get_tags(raw):
    tags = re.compile(
        '(<.*?>)|((?<=>).*?(?=<))')
    return re.findall(tags, raw)


without_spaces = de_shitter(data)

tags_array = get_tags(without_spaces)
p = []

for item in tags_array:
    p.append(sorted(list(item), reverse=True)[0])

print(''.join(p) == without_spaces)
# p=''

# ii = 1
# print(type(tags_array[0]))
#
# print(map(tags_array,lambda x: type(x)))
#
#
# # print(tags_array)
