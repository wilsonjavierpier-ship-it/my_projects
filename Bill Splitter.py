running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print(f'Total bill so far: {running_total}')

tip = running_total * 0.25
print(f'Tip amount: {tip}')

per_person_total = (running_total + tip) / num_of_friends
print(f'Each person should pay: {per_person_total}')

final_bill = 62.13437499999999
rounded_final_bill = round(final_bill, 2)
print(f'Final bill rounded to two decimal places: {rounded_final_bill}')