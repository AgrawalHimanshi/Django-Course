import re


patters=['term1', 'term2']
text='this is a string with term1, not the other'

for pattern in patters:
    print('i am searching for '+pattern)
    #search function doesn't return bool value,
    #it return special match object which contains
    #information about MATCH
    #match.end() and match.start

    if re.search(pattern,text):
        match=re.search(pattern,text)
        print("MATCH!")
        print(match.start())
    else:
        print("NOT MATCH!")

#pattern splitting
split_term='@'
email='user@gmail.com'
print(re.split(split_term,email))

#find all instances of method in a string
print(re.findall('match','test to find match in match string'))


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('searching for pattern {} '.format(pat))
        print(re.findall(pat,phrase))

test_phrase="sd..sdd..dsss..sdsd"
test_pat=['s[sd]+'] #s followed by either 1 or more s or d
# ^ - don't include
# [^] - start with
# [sd] - either s or d
# + - 1 or more
# * - 0 or more
# ? - o or 1
# {3} - exact 3 d's
# {1,3} - 1 to 3 d's
# r'\D+' - not digit
# r'\d+' -digits
# r'\s+'- white spaces
# r'\S+' - not a white spaces
# r'\w+' - all alphanumeric
# r'\W+' - not alphanumeric

multi_re_find(test_pat,test_phrase)
test_phrase2='this is a, punctuation! sentence.'
test_pat2= ['[^!.,?]+']
multi_re_find(test_pat2,test_phrase2)
