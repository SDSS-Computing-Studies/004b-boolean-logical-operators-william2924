#! python3

number = int(input())
if number % 6 == 0 and number % 8 != 0:
    print(str(number) + " is frue")
else:
    print(str(number) + " is not frue")