

# bill = 75
# if bill 
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')

# number=3
# if (number %2) == 0:
#      print('Even')
# else:
#      print('Odd')


# bill=100
# Service = input("How was the service? ")
# if Service == "bad":
#     print(bill)
# if Service == "okay":
#     bill =+ 1.15*bill
#     print(bill)
# if Service == "good":
#     bill =+ 1.20*bill
#     print(bill)
# if Service == "great":
#     bill =+ 1.25*bill
#     print(bill)

def find_factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

number = int(input("Insert a number. "))
factors = find_factors(number)
print(factors)