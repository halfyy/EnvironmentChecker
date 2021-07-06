# Задача: реализовать бота который сможет отправлять данные о комнате по запросу от пользователя.
# Большим плюсом будет считаться реализация дополнительных функций, например:
#
# 1) Статистика по всем комнатам и нормам в них.
# 2) Цветовой индикатор по комнате (например красный если в комнате больше половины индикаторов вне нормы) -
#    бот может отправлять соответствующую картинку например.
# 3) Создайте различные команды которые будут получать данные со всех комнат, или например тех, что в правом крыле
#    и наоборот.
# 4) Придумайте как можно сделать интерфейс приятнее и удобнее для пользователя.
# 5) Проявите креативность, добавьте новые функции на ваше усмотрение - это также учитывается.


# ['Название Комнаты', 'Температура', 'Уровень шума в dB', 'Концентрация СО2', 'Уровень освещенности']
Rooms = [
    ['Cafeteria', '19 Celsius', '20 dB', '497 ppm', '127 lux'],
    ['Storage', '20 Celsius', '89 dB', '470 ppm', '221 lux'],
    ['Weapons', '36 Celsius', '29 dB', '424 ppm', '150 lux'],
    ['O2', '26 Celsius', '30 dB', '533 ppm', '186 lux'],
    ['Admin', '36 Celsius', '38 dB', '418 ppm', '156 lux'],
    ['Communication', '32 Celsius', '66 dB', '508 ppm', '79 lux'],
    ['Shields', '27 Celsius', '51 dB', '382 ppm', '326 lux'],
    ['Navigation', '26 Celsius', '40 dB', '300 ppm', '289 lux'],
    ['Electrical', '31 Celsius', '50 dB', '446 ppm', '292 lux'],
    ['MedBay', '34 Celsius', '24 dB', '330 ppm', '227 lux'],
    ['UpperEngine', '25 Celsius', '29 dB', '588 ppm', '313 lux'],
    ['LowerEngine', '33 Celsius', '48 dB', '540 ppm', '171 lux'],
    ['Reactor', '28 Celsius', '39 dB', '315 ppm', '285 lux'],
    ['Security', '21 Celsius', '36 dB', '411 ppm', '289 lux']
]

# Нормы температуры, уровня шума, концентрации СО2 и уровня освещенности
norms = [range(20, 27), range(20, 42), range(380, 420), range(200, 300)]
