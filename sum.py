all_tickets = int(input('Введите количество билетов: '))

# Создаем list, в котором будет храниться возраст участников
numbers_ages = []

# для каждого билета запросить возраст
# Заполняем numbers_ages числами, которые вводит пользователь
for i in range(0, all_tickets):
    input_value = int(input(f'Введите возраст участника №{i + 1}:\n'))
    numbers_ages.append(input_value)

# исходя из возраста выбираем стоимость билета
    def prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

# считаем стоимость всех билетов
    full_prise = sum(map(prise, numbers_ages))

# проводим скидку если количество билетов больше 3
discount_prise = int(full_prise * 0.9)
if all_tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount_prise, "руб.")
else:
    print('Стоимость всех билетов: ', full_prise, "руб.")
