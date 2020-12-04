def arithmetic_arranger(problems, b=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    spaces = []
    firstLine = []
    secondLine = []
    thirdLine = []
    fourthLine = []
    s = 0
    for problem in problems:
        equation = problem.split()
        spaces.append(max(len(equation[0]), len(equation[2])) + 2)
        if not equation[0].isdigit() or not equation[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if equation[1] != '+' and equation[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if spaces[s] > 6:
            return 'Error: Numbers cannot be more than four digits.'
        if equation[1] == '+':
            equation.append(str(int(equation[0]) + int(equation[2])))
        if equation[1] == '-':
            equation.append(str(int(equation[0]) - int(equation[2])))
        for i in range(spaces[s]):
            thirdLine.append('-')
            if i == 0:
                secondLine.append(equation[1])
            elif spaces[s] - i > len(equation[2]):
                secondLine.append(' ')
            else:
                secondLine.append(equation[2][len(equation[2]) - spaces[s] + i])

            if spaces[s] - i > len(equation[0]):
                firstLine.append(' ')
            else:
                firstLine.append(equation[0][len(equation[0]) - spaces[s] + i])
            if spaces[s] - i > len(equation[3]):
                fourthLine.append(' ')
            else:
                fourthLine.append(equation[3][len(equation[3]) - spaces[s] + i])
        s += 1
        firstLine.append('    ')
        secondLine.append('    ')
        thirdLine.append('    ')
        fourthLine.append('    ')

    firstLine.pop()
    secondLine.pop()
    thirdLine.pop()
    fourthLine.pop()
    firstLine.append('\n')
    secondLine.append('\n')
    if not b:
        return "".join(firstLine) + "".join(secondLine) + "".join(thirdLine)
    thirdLine.append('\n')
    return "".join(firstLine) + "".join(secondLine) + "".join(thirdLine) + "".join(fourthLine)
