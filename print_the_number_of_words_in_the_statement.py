# input user's statement
user_statement = input("Please input a statement: ")
# split the statement to single words then count the words
splitted_statement= user_statement.split(' ')
number_of_words= len(splitted_statement)
# print the number of words
print (number_of_words)