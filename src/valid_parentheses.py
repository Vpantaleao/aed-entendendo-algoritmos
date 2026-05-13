from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    test_stack = MyStack()
    mapping = {")": "(", "]": "[", "}": "{"}

    for i in string:
        if i in mapping:
            top = test_stack.pop()

            if mapping[i] != top:
                return False
            
        else:
            test_stack.push(i)

    return test_stack.is_empty()


