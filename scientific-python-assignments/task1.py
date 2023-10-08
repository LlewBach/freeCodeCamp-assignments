import sys
import re

# Arguments
tasklist = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
dosums = False

# Elements
operators = []
number1s = []
number2s = []
answerlist = []
# Space control
totalwidth = []
num1spaces = []
num2spaces = []
# Line builders
line1parts = []
line2parts = []
answerlineparts = []


# Catching too many problems
if len(tasklist) > 5 :
    print('Error: Too many problems.')
    sys.exit()


# Filling operators, numbers, totalspaces, numberspaces
for problem in tasklist:
    if '+' in problem :
        operators.append('+')
    elif '-' in problem :
        operators.append('-')

# don't need try clause as regex no match with not throw error
    try :
        parts = re.split(r'[+\-]', problem)
    except : 
        print('Error: Operator must be '+' or '-'.')

    num1string = parts[0].strip()
    num2string = parts[1].strip()

# Catching non-number strings
    try :
        num1 = int(num1string)
        num2 = int(num2string)
    except :
        print('Error: Numbers must only contain digits.')
        sys.exit()

# Setting dashwidth
    dashwidth = None
    if num1 > num2 :
        dashwidth = len(num1string) + 2
    else :
        dashwidth = len(num2string) + 2
    

# setting max charwidth
    if dashwidth > 6 : 
        print('Error: Numbers cannot be more than four digits.')
        sys.exit()


# Calculating spaces for num1 and num2
    num1space = dashwidth - len(num1string)
    num2space = dashwidth - len(num2string) - 1

    number1s.append(num1)
    number2s.append(num2)
    totalwidth.append(dashwidth)
    num1spaces.append(num1space)
    num2spaces.append(num2space)


# Create line parts
for i in range(len(number1s)) :
# Filling answer lists
    if operators[i] == '+' :
        answerlist.append(number1s[i] + number2s[i])
    else :
        answerlist.append(number1s[i] - number2s[i])

    string1 = f"{' ' * num1spaces[i]}{number1s[i]}{' ' * 4}"
    string2 = f"{operators[i]}{' ' * num2spaces[i]}{number2s[i]}{' ' * 4}"
    astring = f"{' ' * (totalwidth[i] - len(str(answerlist[i])))}{answerlist[i]}{' ' * 4}"
    line1parts.append(string1)
    line2parts.append(string2)
    answerlineparts.append(astring)


# Assembling line parts
finalline1 = ''
finalline2 = ''
finaldashes = ''
finalanswerline = ''
for j in range(len(line1parts)) :
    finalline1 += line1parts[j]
    finalline2 += line2parts[j]
    finaldashes += ('-' * totalwidth[j] + ' ' * 4)    
    finalanswerline += answerlineparts[j]
    

print(finalline1)
print(finalline2)
print(finaldashes)
if dosums :
    print(finalanswerline)

    