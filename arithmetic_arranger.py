import sys

def arithmetic_arranger(problems, results=False):
    top = ""
    bottom = ""
    dashes = ""
    sol_f = ""
    if len(problems) > 5:
        return "Error: Too many problems."
        sys.exit(0)

    for x, y in enumerate(problems):
        y = y.split(' ')

        if y[0].isdigit() is False:
            return "Error: Numbers must only contain digits."
            sys.exit(0)
        if y[2].isdigit() is False:
            return "Error: Numbers must only contain digits."
            sys.exit(0)

        res = max(y, key=len)
        sol = (' '.join(y))
        solutions = eval(sol)

        if len(res) > 4:
            return "Error: Numbers cannot be more than four digits."
            sys.exit(0)

        if y[1] == "*":
            return "Error: Operator must be '+' or '-'."
        if y[1] == "/":
            return "Error: Operator must be '+' or '-'."

        if len(y[0]) < len(y[2]):                   
            b4_spaces = len(y[2]) + 2               
            lgth_sol = len(str(solutions))          
            rw1_space = b4_spaces - len(y[0])       
            w = " " * rw1_space                     
            top += w + y[0] + "    "
            bottom += y[1] + " " + y[2] + "    "
            dashes += b4_spaces * "-" + "    "
            sol_f += " " * (b4_spaces - lgth_sol) + str(solutions) + "    "

        if len(y[0]) == len(y[2]):
            b4_spaces = len(y[0]) + 2
            rw1_space = b4_spaces - len(y[0])
            w = " " * rw1_space
            top += w + y[0] + "    "
            bottom += y[1] + " " + y[2] + "    "
            dashes += b4_spaces * "-" + "    "
            sol_f += w + str(solutions) + "    "

        if len(y[0]) > len(y[2]):
            w = " " * ((len(y[0]) + 2) - (len(y[2]) + 1))
            lgth_sol = len(str(solutions))  # 4
            top += "  " + y[0] + "    "
            bottom += y[1] + w + y[2] + "    "
            dashes += (len(y[0]) + 2) * "-" + "    "
            sol_f += ((len(y[0]) + 2) - lgth_sol) * " " + str(solutions) + "    "

    top = top.rstrip()
    top += top.join("\n")
    bottom = bottom.rstrip()
    bottom += bottom.join("\n")
    dashes = dashes.rstrip()
    sol_f = sol_f.rstrip()

    if results:
        dashes += dashes.join("\n")
        return top + bottom + dashes + sol_f

    else:
        return top + bottom + dashes