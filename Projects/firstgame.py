import random
#GET GUESS
def get_guess():
    return list(input('what is your guess'))
#GENERATE COMPUTER CODE
def generate_code():
    digits=[str(n) for n in range(10)]
    #suffle digits
    random.shuffle(digits)
    return digits[:3]
# GENERATE CLUES

def generate_clues(code,user_guess):
    if user_guess==code:
        return "CODE CRACKED"

    clues=[]
    for ind, num in enumerate(user_guess):
        if num==code[ind]:
            clues.append( "match")
        elif num in code:
            clues.append("close")

    if clues==[]:
        return ["Nope"]
    else:
        return clues

# RUN CODE
print('hello code breaker!')
secret_code=generate_code()

clues=[]

while clues != "CODE CRACKED":
    guess=get_guess()
    clues=generate_clues(secret_code,guess)
    print("your guess is: ")
    for cl in clues:
        print(cl)
