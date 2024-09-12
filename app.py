

# bill = 75
# if bill 
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')

number=7
if (number %2) == 0:
     print('Even')
else:
     print('Odd')
bill=100



Service = input("How was the service? ")
if Service == "bad":
    print(bill)
if Service == "okay":
    bill =+ 1.15*bill
    print(bill)
if Service == "good":
    bill =+ 1.20*bill
    print(bill)
if Service == "great":
    bill =+ 1.25*bill
    print(bill)