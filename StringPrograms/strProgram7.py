# Python – Convert Snake case to Pascal case
# strProgram7.py

snake_case_str = "this_is_a_variable"
words = snake_case_str.split("_")
print(words)
pascal_str = "".join([w.capitalize() for w in words])
print(f"pascal str {pascal_str}")