# input a 1-1000 number
inputted_number= int(input("Please input a number from 1-1000: "))
# loop: while the number's length is less than 6 add zero at the beggining
if 1<= inputted_number <= 1000:
    six_digit_number= str(inputted_number)
    while len(six_digit_number) != 6:
        six_digit_number= "0" + six_digit_number
    # print the inputed number in 6 digit format
    print (six_digit_number)