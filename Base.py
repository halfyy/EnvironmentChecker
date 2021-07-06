# -*- coding: utf-8 -*-

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
# ['Название класса', 'Количество учеников', 'Ученик1', 'Ученик2', 'Ученик3'...]
Classes = [
    ['1class', '18', 'Вася Пупкин', 'Илья Муромец', 'Даниил Кирасов','Юлия Смирнова', 'Михаил Волков', 'Лев Алексеев', 'Виктор Панин', 'София Лобанова','Георгий Новиков', 'Александр Кудрявцев', 'Михаил Никитин', 'Андрей Тихонов', 'Камилла Коровина', 'Филипп Коротков', 'Григорий Фирсов', 'Максим Кондрашов', 'Ульяна Яковлева', 'Александр Дорохов'],
    ['2class', '17', 'Генадиев Горин', 'Богдан Говор', 'Иван Великий', 'Агния Михайлова', 'София Фомина', 'Виктор Данилов', 'Кира Полякова', 'Ева Петрова', 'Артур Попов', 'Максим Прокофьев', 'Полина Сычева', 'Алиса Кузнецова', 'Илья Макаров', 'Кирилл Митрофанов', 'Борис Мухин', 'Артём Зуев', 'Вероника Иванова'],
    ['3class', '17', 'Владислав Романов', 'Николай Басков', 'Анастасия Жманская'],
    ['4class', '15', 'Александр Фадеев', 'Виктория Борисова', 'Дарья Николаева', 'Григорий Марков', 'Мария Гончарова', 'Фёдор Хромов', 'Иван Лобанов', 'Ульяна Королева','Матвей Поляков', 'Даниил Чесноков', 'Владимир Фомин', 'Арина Прохорова', 'Полина Королева', 'Кристина Михеева', 'Тихон Константинов'],
    ['5class', '20', 'Анастасия Юдина', 'Алексей Степанов', 'Пётр Крылов', 'Алиса Олейникова', 'Вера Чернышева', 'Дмитрий Калачев', 'Иван Козлов', 'Ольга Антипова', 'Артём Федотов', 'Данила Балашов', 'Альбина Макарова', 'Василиса Тихомирова', 'Аделина Орлова', 'София Максимова', 'Пётр Попов', 'Владимир Королев', 'Марат Соколов', 'Андрей Федоров', 'Артём Кондратьев', 'Ульяна Овчинникова'],
    ['6class', '19', 'Яков Попов', 'Александр Ларин', 'Данила Кочетков', 'Алина Некрасова', 'Анна Фомина', 'Алиса Яковлева', 'Милана Петрова', 'Полина Козлова', 'Всеволод Сорокин', 'Анна Куликова', 'Тимофей Грибов', 'Милана Васильева', 'Николай Киселев', 'Роман Третьяков', 'Вероника Карпова', 'Алёна Еремина', 'Вера Казакова', 'София Прохорова', 'Артём Мартынов'],
    ['7class', '18', 'Ева Андреева', 'Роман Болдырев', 'Даниэль Пирогов', 'Евгений Егоров', 'Мария Кулешова', 'Дарья Борисова', 'Евгений Старостин', 'Елизавета Давыдова', 'Артём Мальцев', 'Мирон Сычев', 'Иван Петров', 'Ева Ежова', 'Валерия Моисеева', 'Матвей Смирнов', 'Роман Козлов', 'Николай Леонов', 'Мария Наумова','Виктория Козина'],
    ['8class', '20', 'Вероника Соловьева', 'Денис Воробьев', 'Алексей Потапов', 'Анна Столярова', 'Мария Любимова', 'Маргарита Григорьева', 'Роман Попов', 'Егор Круглов', 'Никита Давыдов', 'Михаил Медведев', 'Фёдор Коновалов', 'Степан Петров', 'Фёдор Жданов', 'Мила Савельева', 'Валерий Краснов', 'Алиса Шаповалова', 'Павел Черный', 'Надежда Тарасова', 'Марк Калугин', 'Ариана Ткачева'],
    ['9class', '17', 'Матвей Соловьев', 'Николай Минаев', 'Полина Богомолова', 'Андрей Ковалев', 'Тимур Ермаков', 'Ксения Васильева', 'Таисия Лопатина', 'Мария Карпова', 'Алексей Галкин', 'Анастасия Анохина', 'Анастасия Исаева', 'Марк Дорофеев', 'Милана Павлова', 'Малика Савельева', 'Игорь Тарасов', 'Дарья Федорова', 'Елисей Никифоров'],
    ['9class', '20', 'Сергей Горбунов', 'Софья Сухова', 'Анастасия Волкова', 'Мадина Воробьева', 'Алёна Лопатина', 'Всеволод Широков', 'Александр Алексеев', 'Ева Павловская', 'Александр Семенов', 'Данил Борисов', 'Ксения Сазонова', 'Дмитрий Сидоров', 'Михаил Баженов', 'Сергей Казаков', 'Илья Орлов', 'Эмин Афанасьев', 'Ольга Дьякова', 'Максим Морозов','Глеб Новиков', 'Таисия Захарова'],
    ['10class', '15', 'Игорь Куликов', 'Ева Смирнова', 'Денис Стариков', 'Дмитрий Гуров', 'София Павлова', 'Фёдор Клюев', 'Ярослав Дмитриев', 'Николь Михайлова', 'Матвей Давыдов', 'Давид Иванов', 'Марк Васильев', 'Семён Дмитриев', 'Елизавета Медведева', 'Юлия Голованова', 'Полина Герасимова'],
    ['11class', '16', 'Марьяна Смирнова', 'Вадим Михайлов', 'Вера Орлова', 'Маргарита Яковлева', 'Ника Горбунова', 'Ярослава Широкова', 'Алиса Попова', 'Семён Жуков', 'Милана Овчинникова', 'Екатерина Васильева', 'Каролина Троицкая', 'Николай Колесников', 'Екатерина Самсонова', 'София Фирсова', 'Ирина Демидова', 'Григорий Комиссаров'],
    ['12class', '18', 'Аяна Круглова', 'Валерия Сухарева', 'Павел Лебедев', 'Дарья Мешкова', 'Александр Беляев', 'Марк Евсеев', 'Лев Сорокин', 'Елизавета Дубова', 'Матвей Павловский', 'Савва Федоров', 'София Карпова', 'Амина Фомина', 'Дмитрий Ершов', 'Мария Нефедова', 'Анна Соловьева', 'Максим Булгаков', 'Кирилл Грачев', 'Елизавета Горшкова'],
    ['13class', '21', 'Александр Шубин', 'Валерия Некрасова', 'Степан Пономарев', 'Егор Морозов', 'Николай Власов', 'Давид Зверев', 'Варвара Артамонова', 'Михаил Андреев', 'Артём Белоусов', 'Арсений Соколов', 'Артём Сазонов', 'Алексей Федоров', 'Ульяна Лебедева', 'Демид Медведев', 'София Гордеева', 'Денис Сидоров', 'Владимир Евсеев', 'Валерия Ситникова', 'Даниил Васильев', 'Михаил Майоров', 'Аделина Емельянова']
]
# Нормы температуры, уровня шума, концентрации СО2 и уровня освещенности
norms = [range(20, 27), range(20, 42), range(380, 420), range(200, 300)]