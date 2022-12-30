# Compiler Construction Assignment
# Faraz Ahmad Qureshi [reg no: 200901045]
# BSCS - 01

import re
import ast

#regular expressions that we will use
token_spec = [r'\d+(\.\d+)?', # identify any no. of digits
              r'[a-zA-z]+',   # identify any identifer(character)
              r'[+\-*/]',     # identify any operator
              r'[()]',        # identify parenthesis
              r'[ \t]+']      # whitespaces,tabs

Identifiers = []
Constants = []
Operators = []
Brackets = []
def lexical_analyzer(text):
    tokens = []
    
    token_list = ('ID','CONST','OP','LP','RP')
    print("\n[|Lexical Analyzer|]\n")
    for x in text:
        if re.findall(token_spec[0],x):
            print(x," is a Digit ")
            tokens.append(token_list[1])
            Constants.append(x)
        elif re.findall(token_spec[1],x):
            print(x," is an Identifier")
            tokens.append(token_list[0])
            Identifiers.append(x)
        elif re.findall(token_spec[2],x):
            print(x,"is an Operator")
            tokens.append(token_list[2])
            Operators.append(x)
        elif re.findall(token_spec[3],x):
            if x == '(': 
                print(x,"is Left Parenthesis")
                tokens.append(token_list[3])
                Brackets.append(x)
            elif x == ')': 
                print(x,"is Right Parenthesis")
                tokens.append(token_list[4])
                Brackets.append(x)
        elif re.findall(token_spec[4],x):
            print(x,"Whitespace")
        else:
            print("Erorr! ", x + " is not part of language")
    print(tokens)

input_choice = input("Press:\n[A] to auto-enter expression\n[B] to type expression yourself: ")
if input_choice == 'A' or input_choice == 'a':
    txt = 'a + (b*c)'
elif input_choice == 'B' or input_choice =='b':
    txt = input("\nPlease enter an expression to be tokenized and evaluated: ")
else: print("\nwrong choice entered...\n")
#txt = "a+(b*c)"
txt = re.sub(r'\s+', '', txt) #simple regex to remove whitespaces
lexical_analyzer(txt)
print(list(txt))
print(f"\nIdentifers: {Identifiers}\nDigits: {Constants}\nOperators: {Operators}\nParenthesis: {Brackets}\n")

code = ast.parse(txt, mode='eval')   # parse the expression
print("\n[|Expression Tree|]\n")
print(ast.dump(code))                # print the AST