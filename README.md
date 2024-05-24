#For reading an integer from the input given.


if __name__ == '__main__':
    n = int(input().strip())
    
#I am checking if the integer is odd or not in "if" condition. "Else" is for the opposite.

    if n % 2 == 1:
        print("Weird")

    else: 
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")