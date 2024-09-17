

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

# def find_factors(x):
#     factors = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             factors.append(i)
#     return factors

# def find_factors(num):
#      factors = []
#      for i in range(1, num + 1):
#          if num % i == 0:
#              factors.append(i)
#      return factors

commonfactors = []
def find_factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
        ret
def find_factors2(y):
    factors2 = []
    for i in range(1, y + 1):
        if y % i == 0:
            factors2.append(i)
            if i in factors and factors2:
                commonfactors.append(i)
        return factors2
number = int(input("Insert the 1st number. "))
number2 = int(input("Insert the 2nd number. "))
factors = find_factors(number)
factors2 = find_factors2(number2)
gcf = commonfactors[-1]
print(gcf)

# if y and x have i as a factor append to common factors list.