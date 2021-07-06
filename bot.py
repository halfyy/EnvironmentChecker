# -*- coding: utf-8 -*-


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from Requirements import Rooms, norms
import emoji


def norm_checker(i, x):
    word_list = i[x].split()
    for word in word_list:
        if word.isnumeric():
            temp = (int(word))
            break
    if temp in norms[x - 1]:
        temp_status = ' ✅'
    else:
        temp_status = ' ❌'
    return temp_status


def sort_f(x):
    i = Rooms
    for c in range(len(i)):
        for j in range(len(i)):
            for k in range(j + 1, len(i), 1):
                word_list = i[j][x].split()
                for word in word_list:
                    if word.isnumeric():
                        temp1 = (int(word))
                        break
                word_list = i[k][x].split()
                for word in word_list:
                    if word.isnumeric():
                        temp2 = (int(word))
                        break
                if temp1 > temp2:
                    i[j], i[k] = i[k], i[j]
    return i


TOKEN = '1710168407:AAEO5D0JvjbuxewP26I9igTUPCxxVUcEssM'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

room_list = ["Cafeteria", "Storage", "Weapons", "O2", "Admin", "Communication", "Shields", "Electrical", "MedBay",
             "UpperEngine", "LowerEngine", "Reactor", "Security"]

button1 = KeyboardButton('Левое крыло')
button2 = KeyboardButton('Центральная часть')
button3 = KeyboardButton("Правое крыло")
button4 = KeyboardButton("План")
button5 = KeyboardButton("Общая информация")

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row(button1, button2, button3)
keyboard1.row(button4, button5)

# Выбор комнаты

electrical_btn = KeyboardButton('Electrical')
medbay_btn = KeyboardButton('MedBay')
upperengine_btn = KeyboardButton('UpperEngine')
lowerengine_btn = KeyboardButton('LowerEngine')
reactor_btn = KeyboardButton('Reactor')
security_btn = KeyboardButton('Security')

keyboard_left_side = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_left_side.row(electrical_btn, medbay_btn, upperengine_btn, lowerengine_btn, reactor_btn, security_btn)

cafeteria_btn = KeyboardButton('Cafeteria')
storage_btn = KeyboardButton('Storage')

keyboard_center_side = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_center_side.row(cafeteria_btn, storage_btn)

weapons_btn = KeyboardButton('Weapons')
o2_btn = KeyboardButton('O2')
admin_btn = KeyboardButton('Admin')
communication_btn = KeyboardButton('Communication')
shields_btn = KeyboardButton('Shields')

keyboard_right_side = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_right_side.row(weapons_btn, o2_btn, admin_btn, communication_btn, shields_btn)

# Сортировка
temp_btn = KeyboardButton('Сортировать по температуре')
sound_btn = KeyboardButton('Сортировать по уровню звука')
co2_btn = KeyboardButton('Сортировать по концентрации CO2')
light_btn = KeyboardButton('Сортировать по уровню освещённости')
full_info_btn = KeyboardButton('Полная информация о кабинетах')

keyboard_sort = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_sort.row(temp_btn, sound_btn)
keyboard_sort.row(co2_btn, light_btn)
keyboard_sort.row(full_info_btn)

keyboard_empty = ReplyKeyboardRemove()


@dp.message_handler(commands=["start"])
async def start_cmd_handler(message: types.Message):
    await message.reply("Вас приветствует Бот лагеря Among Us!\n\n Информацию о какой части корабля вы хотите узнать?",
                        reply_markup=keyboard1)


@dp.message_handler(text=['Левое крыло', "Правое крыло", "Центральная часть"])
async def checker(message: types.Message):
    zone_name = message.text
    if zone_name == 'Левое крыло':
        await message.reply("Какую комнату хотите выбрать?", reply_markup=keyboard_left_side)
    elif zone_name == 'Центральная часть':
        await message.reply("Какую комнату хотите выбрать?", reply_markup=keyboard_center_side)
    elif zone_name == 'Правое крыло':
        await message.reply("Какую комнату хотите выбрать?", reply_markup=keyboard_right_side)


@dp.message_handler(text='План')
async def plan_send(message: types.Message):
    with open('map.jpg', 'rb') as photo:
        await message.reply_photo(photo)

@dp.message_handler(text=room_list)
async def room_choose(message: types.Message):
    flag = False
    msg_text = ""
    room_name = message.text
    room_index = room_list.index(room_name)
    for i in range(1, 5, 1):
        temp_status = norm_checker(Rooms[room_index + 1], i)
        if temp_status == ' ❌':
            flag = True
        msg_text += Rooms[room_index + 1][i] + temp_status + '\n'
    if flag == True:
        msg_text += "Класс не готов  ❌ \n"
    else:
        msg_text += "Класс готов  ✅\n"
    await message.reply(msg_text, reply_markup=keyboard_empty)


@dp.message_handler(text="Общая информация")
async def main_info(message: types.Message):
    await message.reply("Что вы хотите узнать?", reply_markup=keyboard_sort)


@dp.message_handler(
    text=['Сортировать по температуре', 'Сортировать по уровню звука', 'Сортировать по концентрации CO2',
          'Сортировать по уровню освещённости'])
async def sorter(message: types.Message):
    msg_text = ""
    if message.text == 'Сортировать по температуре':
        mass = sort_f(1)
        for i in range(len(mass)):
            flag = False
            msg_text += mass[i][0] + "\n"
            temp_status = norm_checker(mass[i], 1)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Температура: " + mass[i][1] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 2)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень шума: " + mass[i][2] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 3)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Концентрация CO2: " + mass[i][3] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 4)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень освещённости: " + mass[i][4] + temp_status + '\n\n'
            if flag == True:
                msg_text += "Класс не готов  ❌ \n\n"

            else:
                msg_text += "Класс готов  ✅\n\n"
    elif message.text == 'Сортировать по уровню звука':
        mass = sort_f(2)
        for i in range(len(mass)):
            flag = False
            msg_text += mass[i][0] + "\n"
            temp_status = norm_checker(mass[i], 1)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Температура: " + mass[i][1] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 2)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень шума: " + mass[i][2] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 3)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Концентрация CO2: " + mass[i][3] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 4)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень освещённости: " + mass[i][4] + temp_status + '\n\n'
            if flag == True:
                msg_text += "Класс не готов  ❌ \n\n"

            else:
                msg_text += "Класс готов  ✅\n\n"
    elif message.text == 'Сортировать по концентрации CO2':
        mass = sort_f(3)
        for i in range(len(mass)):
            flag = False
            msg_text += mass[i][0] + "\n"
            temp_status = norm_checker(mass[i], 1)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Температура: " + mass[i][1] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 2)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень шума: " + mass[i][2] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 3)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Концентрация CO2: " + mass[i][3] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 4)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень освещённости: " + mass[i][4] + temp_status + '\n\n'
            if flag == True:
                msg_text += "Класс не готов  ❌ \n\n"

            else:
                msg_text += "Класс готов  ✅\n\n"
    else:
        mass = sort_f(4)
        for i in range(len(mass)):
            flag = False
            msg_text += mass[i][0] + "\n"
            temp_status = norm_checker(mass[i], 1)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Температура: " + mass[i][1] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 2)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень шума: " + mass[i][2] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 3)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Концентрация CO2: " + mass[i][3] + temp_status + '\n'
            temp_status = norm_checker(mass[i], 4)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень освещённости: " + mass[i][4] + temp_status + '\n\n'
            if flag == True:
                msg_text += "Класс не готов  ❌ \n\n"

            else:
                msg_text += "Класс готов  ✅\n\n"
    await message.reply(msg_text, reply_markup=keyboard_empty)


@dp.message_handler(text="Полная информация о кабинетах")
async def full_info(message: types.Message):
    mc = [[], [], [], [], []]
    msg_text = ""
    for i in Rooms:
        c = 0
        temp_status = norm_checker(i, 1)
        if temp_status == ' ❌':
            c += 1
        temp_status = norm_checker(i, 2)
        if temp_status == ' ❌':
            c += 1
        temp_status = norm_checker(i, 3)
        if temp_status == ' ❌':
            c += 1
        temp_status = norm_checker(i, 4)
        if temp_status == ' ❌':
            c += 1
        mc[c].append(i)
    for i in range(5):
        for j in range(len(mc[i])):
            flag = False
            msg_text += mc[i][j][0] + "\n"
            temp_status = norm_checker(mc[i][j], 1)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Температура: " + mc[i][j][1] + temp_status + '\n'
            temp_status = norm_checker(mc[i][j], 2)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень шума: " + mc[i][j][2] + temp_status + '\n'
            temp_status = norm_checker(mc[i][j], 3)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Концентрация CO2: " + mc[i][j][3] + temp_status + '\n'
            temp_status = norm_checker(mc[i][j], 4)
            if temp_status == ' ❌':
                flag = True
            msg_text += "Уровень освещённости: " + mc[i][j][4] + temp_status + '\n\n'
            if flag == True:
                msg_text += "Класс не готов  ❌ \n\n"

            else:
                msg_text += "Класс готов  ✅\n\n"

    await message.reply(msg_text)


executor.start_polling(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
