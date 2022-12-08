def arithmetic_arranger(problems, s=False):
    arrangedproblems = ""
    if len(problems) > 5:
        arrangedproblems = "Error: Too many problems."
        return arrangedproblems

    #makes a list of operations in string format
    # This splits each variable at position 1 in problems, iterates through them with map and makes a list
    operations = list(map(lambda x: x.split()[1], problems))
    if set(operations) != {"+" or "-"} and len(set(operations)) != 2:
        arrangedproblems = "Error: Operator must be '+' or '-'."
        return arrangedproblems
    #makes a list named numbers
    numbers = []
    for i in problems:  # for each calc in problems
        p = i.split()  # split the strings
        # add the first and last strings to numbers
        numbers.extend([p[0], p[2]])

    # iterates through the list numbers and checks whether all of the values (x) are digits all cheacks whether iterables are true
    if not all(map(lambda x: x.isdigit(), numbers)):
        arrangedproblems = "Error: Numbers must only contain digits."
        return arrangedproblems

    # checks all values and makes sure they are all less than 5 long
    if not all(map(lambda x: len(x) < 5, numbers)):
        arrangedproblems = "Error: Numbers cannot be more than four digits."
        return arrangedproblems

    top = ""
    dash = ""
    # for x in problems evaluate the equation, eval can solve strings
    values = list(map(lambda x: eval(x), problems))
    solutions = ""
    for i in range(0, len(numbers), 2):
        # for the top and bottom numbers finds which is longer then adds two to find the space of the equation
        width = max(len(numbers[i]), len(numbers[i+1])) + 2
        #print(width)
        # adds the top number [i] to the string i formatted to the width
        top += numbers[i].rjust(width)
        dash += "-" * width  # adds the same amount of dashes to the width
        solutions += str(values[i // 2]).rjust(width)  # adds the values
        if i != len(numbers) - 2:  # if i does not = the value of len numbers add 4 " " to the strings
            top += " " * 4
            dash += " " * 4
            solutions += " " * 4
    #print(top)
    bottom = ""
    # range is 1 so that numbers[i] refers to the second number
    for i in range(1, len(numbers), 2):
        width = max(len(numbers[i-1]), len(numbers[i])) + 1
        #print(width, numbers[i-1], numbers[i])
        bottom += operations[i // 2]
        bottom += numbers[i].rjust(width)
        if i != len(numbers) - 1:
            bottom += " " * 4

    if s == True:
        arrangedproblems = "\n".join((top, bottom, dash, solutions))
    else:
        arrangedproblems = "\n".join((top, bottom, dash))

    return arrangedproblems
        

print(arithmetic_arranger(["3 + 855", "988 + 40"]))


