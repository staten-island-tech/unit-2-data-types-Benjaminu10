def find_gcf(x, y):
    common_factors = []
    for i in range(1, min(x, y) + 1):
        if x and y % i == 0 and y % i == 0:
            common_factors.append(i)
    return common_factors[-1]
number = int(input("Insert the 1st number: "))
number2 = int(input("Insert the 2nd number: "))
gcf = find_gcf(number, number2)
print(gcf)