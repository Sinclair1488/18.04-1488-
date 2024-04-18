def check_string_brackets(input_string):
    count1 = 0
    count2 = 0
    if input_string[0] == "(" or input_string[0] == " ":
        for i in input_string:
            if i == "(":
                count1 += 1
            if i == ")":
                count2 += 1
        if count1  == count2:
            return "Yes"
        else:
            return "No"
    else:
        return "No"
print(check_string_brackets("()"))
