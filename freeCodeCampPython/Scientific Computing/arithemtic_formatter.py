def exception_handler(top_var, operand, mid_var):
    try:
        int(mid_var)
        int(top_var)
    except:
        return 'Error: Numbers must only contain digits.'

    try:
        if not(len(top_var) < 5 and len(mid_var) < 5): raise Exception
    except:
        return 'Error: Numbers cannot be more than four digits.'

    try:
        if operand != '+' and operand != '-': raise Exception
    except:
        return 'Error: Operator must be \'+\' or \'-\'.'

    return ''

def arithmetic_arranger(problems, solve=False):
    try:
        if len(problems) > 5:
            raise Exception
    except:
        return 'Error: Too many problems.'

    top = middle = bottom = solved = result = ''
    if solve == True: solved = '\n'
    space = ' '*4
    for p in problems:
        top_var, operand, mid_var = p.split()
        top_len = len(top_var)
        mid_len = len(mid_var)
        max_len = max(top_len, mid_len)

        exceptions = exception_handler(top_var, operand, mid_var)
        if exceptions != '': return exceptions

        top += ' '*(max_len-top_len+2) + top_var + space

        middle += operand + ' '*(max_len-mid_len+1) + mid_var + space

        bottom += '-'*(max_len+2) + space

        if solve:
            top_num = int(top_var)
            mid_num = int(mid_var)
            result = top_num - mid_num
            if operand == '+':
                result = top_num + mid_num
            solved += ' '*(max_len+2-len(str(result))) + str(result) + space
    
    return top.rstrip() + '\n' + middle.rstrip() + '\n' + bottom.rstrip() + solved.rstrip()

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))