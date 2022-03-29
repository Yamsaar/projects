''' Python program to check if the input number is odd or even.
A number is even if division by 2 gives a remainder of 0.
If the remainder is 1, it is an odd number.'''

user_choice = int(input("Hi there, please enter a random intger number:\n"))

if (user_choice % 2) == 0:
    print(user_choice, "is an even number")
else:
    print(user_choice, "is an odd number")
    

        
