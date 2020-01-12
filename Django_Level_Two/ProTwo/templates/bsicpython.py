#lambda operation
numlist=[1,2,3,4,5,6]

result=filter(lambda num: num%2==0,numlist)
print(list(result))
#print("hello")

#check if end of one string contains other string
def endother(a,b):
    a=a.lower()
    b=b.lower()
    return a[-len(b):]==b or a==b[-len(a):]

print(endother('abc','hiabc'))

#double each char of string
def doubleChar(mystring):
    result=''
    for char in mystring:
        result+=char*2
    return result

#take 3 nos. and add them if they are not teen if teen make it 0
#except 15,16
def countSum(a,b,c):
    return fixteen(a)+fixteen(b)+fixteen(c)

def fixteen(a):
    if a [13 14 17 18 19]:
        return 0
    return n
