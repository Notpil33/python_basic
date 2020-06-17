revenue = int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))
if revenue > cost:
    print('Вы получаете прибыль! Выручка больше издержек!')
    profit = revenue - cost
    profitability = profit / revenue
    print(f'Рентабельность выручки: {profitability:.2f}')
elif revenue < cost:
    print('Вы несете убытки! Издержки больше выручки!')
workers_count = int(input('Введите количество сотрудников фирмы: '))
workers_profit = revenue / workers_count
print(f'Прибыль в расчете на одного сотрудника: {workers_profit:.2f}')




