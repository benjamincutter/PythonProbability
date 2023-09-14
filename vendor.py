guaranteed_attendance = 20000

grandstand_attendance = [
    {'count': 20000, 'prob': .25},
    {'count': 50000, 'prob': .5},
    {'count': 80000, 'prob': .25}
]


def get_attendance(attendance: int) -> int:
    return guaranteed_attendance + int(attendance)


audience_purchase = [
    {'percent': .1, 'prob': .6},
    {'percent': .05, 'prob': .39},
    {'percent': .15, 'prob': .01}
]

total_prob = 0
weighted_average = 0
for attendance in grandstand_attendance:
    for purchase in audience_purchase:
        combined_prob = attendance['prob'] * purchase['prob']
        total_prob += combined_prob
        est_attendance = attendance['count']
        total_attendance = get_attendance(est_attendance)
        shirts_sold = int(total_attendance * purchase['percent'])
        weighted_average += (shirts_sold * combined_prob)
        print(f'With {total_attendance} in attendance, sell {shirts_sold} weighted prob {combined_prob}')

print(f'total prob: {total_prob}, sell {weighted_average}')

vendor_options = [
    {'count': 5000, 'cost': 17750, 'per_shirt': round((17750 / 5000), 2)},
    {'count': 7500, 'cost': 25250, 'per_shirt': round((25250 / 7500), 2)},
    {'count': 10000, 'cost': 32125, 'per_shirt': round((32125 / 10000), 2)},
]

sale_price = 100
chunk_size = 12
sale_per_shirt = round(100 / 12, 2)
resale_value = 1.5


for option in vendor_options:
    purchased = option['count']
    for i in range(1, purchased):
        sales = i * sale_per_shirt
        resale = resale_value * (purchased - i)
        revenue = sales + resale
        profit = revenue - option['cost']
        if profit >= 0:
            print(f'{i} sold, {purchased - i} resold, profit: {profit}')
            max_profit = option['count'] * sale_per_shirt - option['cost']
            print(f'max profit: {max_profit}')
            break
