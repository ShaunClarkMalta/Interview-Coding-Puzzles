'''Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.'''

'''Input: String
for char in string:
    if (, [, { -> Append
    elif:
        ) -> Check list[-1]; if (; then pop; else flag and end
'''

def parenthesis_checker(string_to_check):
    valid_string = True
    checker_list = list()
    
    for char in string_to_check:
        if (char == "(") | (char == "[") | (char == "{"):
            checker_list.append(char)
        elif (char == ")") & (checker_list[-1] == "("):
                checker_list.pop(-1)
        elif (char == "]") & (checker_list[-1] == "["):
                checker_list.pop(-1)
        elif (char == "}") & (checker_list[-1] == "{"):
                checker_list.pop(-1)
        else:
              valid_string = False
              return valid_string
    if len(checker_list) == 0:
          return valid_string
    else:
          valid_string = False
          return valid_string
    
test_string1 = "[{()}]"
test_string2 = "[()()]{}"
test_string3 = "([]"
test_string4 = "([{]})"
print(f"Result of Test String 1: {parenthesis_checker(test_string1)}")
print(f"Result of Test String 2: {parenthesis_checker(test_string2)}")
print(f"Result of Test String 3: {parenthesis_checker(test_string3)}")
print(f"Result of Test String 4: {parenthesis_checker(test_string4)}")