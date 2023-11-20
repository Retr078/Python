has_high_income = True
has_good_credit = True

# using the and operator
if has_high_income and has_good_credit:
    print("Eligible for loan")
    
smart = True
good_skill = False

#using the or operator
if smart or good_skill:
    print("can still be programmer")
    
has_criminal_record = False
has_good_credit = True

#using the and not operator
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
