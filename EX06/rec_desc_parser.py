print("Recursive descent parser")
print("E -> +TE' | e\nE' -> +TE' | e\nT -> FT'\nT' -> *FT' | e\nF -> (E) | i\n")

def E():
    T()
    E1()

def E1():
    global look_ahead
    if look_ahead == "+":
        match("+")
        T()
        E1()

def T():
    F()
    T1()

def T1():
    global look_ahead
    if look_ahead == "*":
        match("*")
        F()
        T1()

def F():
    global look_ahead
    if look_ahead == "(":
        match("(")
        E()
        match(")")
    elif look_ahead == 'i':
        match("i")
    else:
        print("Error! Invalid expression.")
        exit()

def match(expected_token):
    global look_ahead
    if look_ahead == expected_token:
        look_ahead = get_next_token()
    else:
        print(f"Error! Expected {expected_token}")
        exit()

def get_next_token():
    global i, token
    if i < len(token) - 1:
        i += 1
        return token[i]
    elif i == len(token) - 1:
        i += 1
        return "$"
    else:
        print("Error! End of input reached unexpectedly.")
        exit()

token = input("Enter tokens: ")
i = 0
look_ahead = token[0]
E()

if look_ahead == "$":
    print("Parsing Successful!")
else:
    print("Error! Invalid expression.")
