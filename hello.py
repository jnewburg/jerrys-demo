import sys

print("Hello World!")
calculated_number = 8 * 5
print(calculated_number)
float_number = 7.0
print(float_number)
my_string = "My age is "
age_string = my_string + "40 years old"
print(age_string)
print("%s and 2 months" % age_string)
print("%d is my favorite float as a decimal" % float_number)
print("%f is my favorite float" % float_number)
print("%s %d years old" % (my_string, calculated_number))
print(my_string + str(float_number))



str_len = len(age_string)
print(age_string)
print(str_len)

num_inst = age_string.count( " years " )
print(num_inst)

sub_string = age_string[2:4]
print(sub_string)

upper_string = age_string.upper()
print(upper_string)
lower_string = age_string.lower()
print(lower_string)
sub_string = age_string[3:9]
print(sub_string)

index_of = age_string.index("years")
print(index_of)

param_0 = sys.argv[0]
param_1 = sys.argv[1]
param_2 = sys.argv[2]

print(param_0)
print(param_1)
print(param_2)



x = 2
print(x == 2)
if x > 1 and x < 3:
    x = x +1
    print(x)
