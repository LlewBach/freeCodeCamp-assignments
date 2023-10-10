def arithmetic_arranger(tasklist, dosums=False):
    import re

    # Arguments
    # tasklist = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    # dosums = True

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
        return 'Error: Too many problems.'


    # Filling operators, numbers, totalspaces, numberspaces
    for problem in tasklist:
        if '+' in problem :
            operators.append('+')
        elif '-' in problem :
            operators.append('-')


        parts = re.split(r'[\+\-]', problem)
        
        if len(parts) < 2:
            return 'Error: Operator must be '+' or '-'.'

        num1string = parts[0].strip()
        num2string = parts[1].strip()

    # Catching non-number strings
        try :
            num1 = int(num1string)
            num2 = int(num2string)
        except :
            return 'Error: Numbers must only contain digits.'

    # Setting dashwidth
        dashwidth = None
        if num1 > num2 :
            dashwidth = len(num1string) + 2
        else :
            dashwidth = len(num2string) + 2
        

    # setting max charwidth
        if dashwidth > 6 : 
            return 'Error: Numbers cannot be more than four digits.'


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
    line1 = ''
    line2 = ''
    dashesline = ''
    answerline = ''
    for j in range(len(line1parts)) :
        line1 += line1parts[j]
        line2 += line2parts[j]
        dashesline += ('-' * totalwidth[j] + ' ' * 4)    
        answerline += answerlineparts[j]

    line1stripped = line1.rstrip()
    line2stripped = line2.rstrip()
    dasheslinestripped = dashesline.rstrip()
    answerlinestripped = answerline.rstrip()
        
    if dosums :
        return f"{line1stripped}\n{line2stripped}\n{dasheslinestripped}\n{answerlinestripped}"
    else:
        return f"{line1stripped}\n{line2stripped}\n{dashesstripped}"
  


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))