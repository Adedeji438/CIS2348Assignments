#Adedeji Akingbola
#PSID:1793979

def exact_change(user_total):
    num_dollars = user_total//100
    num_quarters = (user_total - num_dollars*100)//25
    num_dimes = (user_total - num_dollars*100 - num_quarters*25)//10
    num_nickels = (user_total - num_dollars * 100 - num_quarters * 25 - num_dimes * 10) // 5
    num_pennies = (user_total - num_dollars * 100 - num_quarters * 25 - num_dimes * 10 - num_nickels * 5)

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if num_dollars == 0 and num_quarters == 0 and num_dimes == 0 and num_nickels == 0 and num_pennies == 0:
        print("no change")
    if num_dollars != 0:
        print(str(num_dollars) + " dollars")
    if num_quarters != 0:
        print(str(num_quarters) + " quarter")
    if num_dimes != 0:
        print(str(num_dimes) + " dimes")
    if num_nickels != 0:
        print(str(num_nickels) + " nickels")
    if num_pennies != 0:
        print(str(num_pennies) + " pennies")
