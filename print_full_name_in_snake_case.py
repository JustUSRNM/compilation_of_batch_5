# input user's full name
full_name= input("Please input your full name in incorrect casing: ")
# remove the leading and trailing spaces
no_spaces_full_name= full_name.strip()
# make the full name in lower case
lower_case_full_name= full_name.lower()
# replace the spaces with _
snake_case= lower_case_full_name.replace(' ','_')
# print full name reverse casing
print (snake_case)