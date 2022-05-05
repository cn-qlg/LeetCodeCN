


def input(s :str)-> Boolean:
    stack = list()
    for c in s:
        if c in ["(", "{","["]:
            stack.append(c)
        elif c == ")":
            left = stack.pop()
            if left != "(":
                return False
        elif c == "}":
            left = stack.pop()
            if left != "{":
                return False
        elif c == "]":
            left = stack.pop()
            if left != "[":
                return False
    
    if len(stack) > 0:
        return False
    return True


if __name__ == "__main__":
    pass