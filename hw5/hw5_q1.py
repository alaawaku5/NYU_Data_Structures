from ArrayStack import ArrayStack


def postfix_calc():
    flag = False
    s = ArrayStack()
    var_dict = {}

    while not flag:
        prompt = input('--> ')

        assign_op = False
        operators = "+-*/"
        exp_lst = prompt.split()
        args_stack = ArrayStack()

        for token in exp_lst:
            if token.isalpha():
                if token in var_dict:
                    args_stack.push((var_dict[token]))
                else:
                    assign_op = True
                    var = token
            elif token == "=":
                pass

            elif token.isdigit():
                args_stack.push(int(token))

            elif token in operators:
                arg2 = args_stack.pop()
                arg1 = args_stack.pop()
                if (token == '+'):
                    res = arg1 + arg2
                elif (token == '-'):
                    res = arg1 - arg2
                elif (token == '*'):
                    res = arg1 * arg2
                elif (token == '/'):
                    if (arg2 == 0):
                        raise ZeroDivisionError
                    else:
                        res = arg1 / arg2
                args_stack.push(res)

        if assign_op:
            var_dict[var] = args_stack.top()
            print(var)
        elif prompt == "done()":
            # flag = True
            exit()
        else:
            print(args_stack.top())


a = "5"
print(a.isdigit())
print(postfix_calc())
