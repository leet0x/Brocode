# lambda function = function written in 1 line using lambda keyword
#                     accepts any number of arguments, but only has one expression.
#                     (think of it as a shortcut)
#                     (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(5, 5))
print(add(10, 5, 5))
print(full_name("lee", "kschi"))
print(age_check(19))
