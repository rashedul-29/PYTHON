#Here I am going to practise basic arithmetic operators 

#For taking the input integers

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
#Giving some restraints on the inputs

    
    if 1 <= a <= 10**10 and 1 <= b <= 10**10:
        sum = a + b
        difference = a - b
        multiplication = a*b
        print(sum)
        print(difference)
        print(multiplication)
    else:
        print("Constraints are not fulfilled")