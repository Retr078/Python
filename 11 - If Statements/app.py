is_hot = False
is_cold = False

if is_hot:
    print("It's a beautiful day")
    print("drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("wear warm clothes")
else:
    print("its a lovely day")
    
#Little exercise 

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}") 