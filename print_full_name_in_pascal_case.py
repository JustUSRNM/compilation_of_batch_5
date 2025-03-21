# input user's full name
full_name= input("Please input your full name in incorrect casing: ")
# make the full name into proper casing (title case)
titled_full_name= full_name.title()
# remove the spaces
pascal_case= titled_full_name.replace(' ','')
# print full name in pascal casing
print (pascal_case)