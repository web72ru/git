import csv
import json
import os
import time
# import ast
# import random

# from petrovich.lm_proxer.main import poluchit_spis_godnyh_proxei

import multiprocessing
from os import listdir
from os.path import isfile, join

import requests

session = requests.Session()

следы = 'SNK=116; u__typeDevice=desktop; u__geoUserChoose=1; SIK=dAAAAHXUgCIL46gSoEMKAA; SIV=1; C_mEdw5ztuoe2pf0oEopy6dlcVaqo=AAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D8AAGAhINTpQU5K30hhIfmb_xg-oLUUX3Y; _gcl_au=1.1.908313899.1670042088; tmr_lvid=a33634d191114965d76a871fc4ef16e6; tmr_lvidTS=1670042091534; _gid=GA1.2.75997037.1670042092; _ym_uid=1670042092119446854; _ym_d=1670042092; _ym_isad=1; UIN=dAAAAK7ZmBRIhTdwlEu9Cbuv4R9vDgVCEeOoEpxTCgA; ssaid=d5d727b0-72c3-11ed-af7f-7f9c58b2885d; rrpvid=554093126235759; rcuid=638ad1f27845cfff5fd2dcc8; aplaut_distinct_id=pveK66eGpCE8; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; dd_custom.lastViewedProductImages=[%2212716%22%2C%22%22%2C%22%22]; dd_custom.ts12={%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221670025600%22:12}}; dd_custom.lt11=2022-12-03T07:17:30.376Z; rrlevt=1670051855672; dd__persistedKeys=[%22custom.lastViewedProductImages%22%2C%22custom.lt13%22%2C%22custom.ts14%22%2C%22custom.ts12%22%2C%22custom.lt11%22]; dd_custom.lt13=2022-12-03T08:07:29.014Z; dd_custom.ts14={%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221670025600%22:56}}; digi_uc=W1sidiIsIjYxMTg0NCIsMTY3MDA1MTg1MjE4M10sWyJ2IiwiMTQwMjE3IiwxNjcwMDQ5NDk3NDQyXSxbInYiLCI4MTA0NTkiLDE2NzAwNDI0MDA5OTRdLFsiY3YiLCIxNDAyMTciLDE2NzAwNTQ1NTY1NjJdLFsiY3YiLCI2ODc1MzMiLDE2NzAwNTQ1MzcyNzZdLFsiY3YiLCI2MjMzNTMiLDE2NzAwNDk5Mjc4MTJdLFsiY3YiLCI2NTYxNzIiLDE2NzAwNDk4OTMwNDldLFsiY3YiLCI2MzQwMzkiLDE2NzAwNDk4NDA3NTNdLFsiY3YiLCI5MjY4NzgiLDE2NzAwNDk4MTE1NDldLFsiY3YiLCIxMDE4NDUiLDE2NzAwNDk3Mzc5NzddLFsiY3YiLCIxMjY5MTYiLDE2NzAwNDg3MTU0OTJdLFsiY3YiLCI2NzI1MzAiLDE2NzAwNDgwMzcwNTRdLFsiY3YiLCIxNTA5NjYiLDE2NzAwNDM5NDI1MzBdLFsiY3YiLCIxMDgyMDgiLDE2NzAwNTQ4NDI4MDVdXQ==; u__geoCityGuid=bd10887b-2da4-11df-942d-0023543d7b52; _ga=GA1.2.1071695914.1670042092; __tld__=null; dd__lastEventTimestamp=1670059396857; mindboxDeviceUUID=14c3907a-f9ad-49d9-9d07-6de00b365e20; directCrm-session=%7B%22deviceGuid%22%3A%2214c3907a-f9ad-49d9-9d07-6de00b365e20%22%7D; _ga_XW7S332S1N=GS1.1.1670059181.3.1.1670059603.60.0.0; qrator_msid=1670066563.151.TaCqUhCQudb7FOL9-nqdlqo0q8sgoudbnk153l2nsvv2ou9ke'

заголовки = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'cookie': следы
}

рабочие_прокси = []
# рабочие_прокси = ast.literal_eval(
#     "['188.34.181.148:3897', '31.186.239.244:8080', '101.51.108.165:8080', '89.36.94.242:1337', '163.172.210.222:3897', '95.216.202.146:3128', '116.203.202.160:8443', '213.59.156.119:3128', '85.14.243.31:3128', '185.217.137.241:1337', '163.172.210.222:3897', '62.171.161.88:2018', '185.39.50.2:1337', '161.53.129.23:3128', '23.88.59.122:3128', '3.126.79.210:3128', '64.225.97.57:8080', '158.160.1.43:3128', '208.82.61.66:3128', '134.122.74.46:45678', '47.252.4.64:8888', '185.217.137.242:1337', '34.175.122.75:3128', '93.114.194.26:1337', '158.69.71.245:9300', '50.16.45.86:3129', '95.216.202.146:3128', '89.208.219.121:8080', '39.105.105.240:60080', '151.236.14.178:5678', '164.92.160.38:8080', '115.96.208.124:8080', '35.193.113.186:80', '45.152.188.16:3128', '31.186.239.244:8080', '34.140.197.165:8080', '45.8.179.241:1337', '3.126.79.210:3128', '163.172.210.222:3897', '188.34.181.148:3897']")

УМНОЖИТЕЛЬ_ПРОЦЕССОВ = 1

счётчик_товаров = 1


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def получаем_жсон_словарь(ссылка):
    словарь_жсон = получить_апи_данные(ссылка)
    return словарь_жсон


def получить_кода_городов(строка_запроса):
    print("Получение списка городов")

    города_жсон_словарь = получаем_жсон_словарь(строка_запроса)

    большие_города = города_жсон_словарь['data']['commonCities']
    малые_города = города_жсон_словарь['data']['regionalCities']
    все_города = большие_города + малые_города

    рф_города = []
    коды_городов_1 = {}
    for город in все_города:
        if город['code'] == 'rf':
            рф_города.append(город['title'])
            continue
        коды_городов_1[город['code']] = город['title']
    коды_городов_1['rf'] = ', '.join(рф_города)
    return коды_городов_1


def получить_категории_для_города(код_города):
    print("Обработка города:", код_города)

    # https://api.petrovich.ru/catalog/v2.3/sections/tree/3?city_code=rf&client_id=pet_site
    запрос_к_категориям = 'https://api.petrovich.ru/catalog/v2.3/sections/tree/3'

    парамерты = {
        'city_code': код_города,
        'client_id': 'pet_site'
    }

    словарь_жсон = получить_апи_данные(запрос_к_категориям, парамерты)

    основные_категории = словарь_жсон['data']['sections']
    коды_категорий = []
    for над_категория in основные_категории:
        if 'sections' in над_категория and над_категория['sections']:
            for категория in над_категория['sections']:
                коды_категорий.append([категория['code'], код_города])
    return коды_категорий


def получить_категории_по_городам(коды_городов_1):
    категории_по_городам_1 = []
    i = -1
    for код_города in коды_городов_1:
        i += 1
        if i == 1:  # количество городов для получения категорий
            break
        категории_по_городам_1.extend(получить_категории_для_города(код_города))

    return категории_по_городам_1


def получить_апи_данные(собранный_запрос, параметры=None):
    if параметры is None:
        параметры = {}
    словарь_жсон = {}
    while True:
        # prox = random.choice(рабочие_прокси)
        # proxies = {
        #     'http': prox,
        #     'https': prox
        # }
        try:
            ответ_запроса = session.get(
                собранный_запрос,
                headers=заголовки,
                params=параметры,
                # proxies=proxies,
                timeout=1
            )
        except:
            print(Bcolors.WARNING + "session.get не выполнен" + Bcolors.ENDC, собранный_запрос)
            continue

        if ответ_запроса.status_code != 200:
            print(Bcolors.WARNING + "session.get не выполнен status_code != 200" + Bcolors.ENDC, собранный_запрос)
            continue

        словарь_жсон = json.loads(ответ_запроса.text)

        if not словарь_жсон:
            print(Bcolors.WARNING + "АПИ запрос не выполнен" + Bcolors.ENDC, словарь_жсон)
            continue

        if 'state' in словарь_жсон:
            if 'title' in словарь_жсон['state']:
                title = словарь_жсон['state']['title']
                if title != "ОК" and title != 'Запрос успешно выполнен':
                    print(Bcolors.WARNING + "АПИ запрос не выполнен" + Bcolors.ENDC, словарь_жсон)
                    continue
                else:
                    break  # прерывает бескон
            else:
                print(Bcolors.WARNING + "АПИ запрос не выполнен" + Bcolors.ENDC, словарь_жсон)
                continue
        else:
            print(Bcolors.WARNING + "АПИ запрос не выполнен" + Bcolors.ENDC, словарь_жсон)
            continue
    return словарь_жсон


def получить_список_кодов_товаров_по_категории_и_городу(категория, код_города):
    # категория = категория_код_города[0]
    # код_города = категория_код_города[1]

    print("Получение списка товаров для категории и города:", категория, код_города)

    global список_кодов_товаров

    # https://api.petrovich.ru/catalog/v2.3/sections/12101?limit=20&offset=0&city_code=spb&client_id=pet_site
    запрос_к_списку_товаров = 'https://api.petrovich.ru/catalog/v2.3/sections/'

    начальный_сдвиг = 0
    лимит_апи = 50

    парамерты = {
        'limit': лимит_апи,
        'offset': начальный_сдвиг,
        'city_code': код_города,
        'client_id': 'pet_site'
    }

    собранный_запрос = запрос_к_списку_товаров + str(категория)

    словарь_жсон = получить_апи_данные(собранный_запрос, парамерты)

    список_товаров_1 = словарь_жсон['data']['products']
    количество_товаров = словарь_жсон['data']['pagination']['products_count']

    if количество_товаров > лимит_апи:
        while количество_товаров > лимит_апи:
            начальный_сдвиг += лимит_апи

            парамерты['offset'] = начальный_сдвиг

            словарь_жсон = получить_апи_данные(запрос_к_списку_товаров + str(категория), парамерты)

            список_товаров_1.extend(словарь_жсон['data']['products'])

            количество_товаров -= лимит_апи

    print("Получено:", len(список_товаров_1), 'товаров')

    return код_города, список_товаров_1


def добавить_итог_в_список_кодов_товаров(код_города_список_товаров):
    код_города = код_города_список_товаров[0]
    товары = код_города_список_товаров[1]

    for товар in товары:
        if код_города not in список_кодов_товаров:
            список_кодов_товаров[код_города] = []
        список_кодов_товаров[код_города].append(товар['code'])


def получить_список_всех_товаров(категории_по_городам_1):
    начальное_время = time.time()

    # категории_по_городам_1 = категории_по_городам_1[:1]  # ограничение количества категорий для сбора

    with multiprocessing.Pool(multiprocessing.cpu_count() * УМНОЖИТЕЛЬ_ПРОЦЕССОВ) as p:
        for кат_гор in категории_по_городам_1:
            p.apply_async(получить_список_кодов_товаров_по_категории_и_городу, кат_гор,
                          callback=добавить_итог_в_список_кодов_товаров)

        p.close()
        p.join()

    print("--- %s секунд ---" % (time.time() - начальное_время))


# def записать_коды_товаров(список_кодов_товаров_1):
#     if not os.path.exists(папка_для_кодов_товаров):
#         os.makedirs(папка_для_кодов_товаров)
#
#     общее_товарных_кодов = 0
#     for код_города in список_кодов_товаров_1:
#         список_товарных_кодов = список_кодов_товаров_1[код_города]
#
#         общее_товарных_кодов += len(список_товарных_кодов)
#
#         with open(папка_для_кодов_товаров + '/' + str(код_города) + '.txt', 'w') as f:
#             for код in список_товарных_кодов:
#                 f.write(str(код) + '\n')
#     print("Собрано товаров: ", общее_товарных_кодов)


def получить_данные_на_товар(код_города, код_товара):
    # код_товара = код_города_код_товара[1]
    # код_города = код_города_код_товара[0]

    парамерты = {
        'city_code': код_города,
        'client_id': 'pet_site'
    }

    # https://api.petrovich.ru/catalog/v2.3/products/код_товара?city_code=код_города&client_id=pet_site
    запрос_к_товару = 'https://api.petrovich.ru/catalog/v2.3/products/'
    собранный_запрос = запрос_к_товару + str(код_товара)

    # print("Загрузка товара:", код_товара)
    словарь_жсон = получить_апи_данные(собранный_запрос, парамерты)

    товар = словарь_жсон['data']['product']

    # записать_товар_в_цсв(товар, код_города)

    return [товар, код_города]


# def взять_данные_из_товара(код_товар_спис):
#     код_города = код_товар_спис[0]
#     товар = код_товар_спис[1]
#     данные_товара = {
#         'code': товар['code'],
#         'city_code': код_города,
#         'city': коды_городов[код_города],
#         'title': товар['title'],  # название товара
#         'category_title': товар['section']['title'],  # категория товара
#         'description_no_html': товар['description_no_html']['description'],  # описание товара
#         'weight': товар['weight'],  # вес
#         'height': товар['height'],  # высота
#         'length': товар['length'],  # длина
#         'width': товар['width'],  # ширина
#         'unit_title': товар['unit_title'],  # "шт"
#         'unit_ratio': товар['unit_ratio'],
#         'unit_ratio_alt': товар['unit_ratio_alt'],  # "пог. м"
#         'unit_title_alt': товар['unit_title_alt'],
#         'increment_step': товар['increment_step'],
#
#         # цена
#         'price': товар['price'],  # список
#
#         # характеристики товара
#         'properties': товар['properties'],  # список
#
#         # изображения
#         'images': товар['images'],  # список
#
#         # категории товара
#         'breadcrumbs': товар['breadcrumbs'],  # список
#
#         # дополнительное описание товара
#         'extended_description_no_html': товар['extended_description_no_html'],  # список
#     }
#     return данные_товара


# def записать_товары(код_города):
#     global список_товаров
#
#     if not os.path.exists(папка_для_товарных_данных):
#         os.makedirs(папка_для_товарных_данных)
#
#     with open(папка_для_товарных_данных + '/' + str(код_города) + '.csv', 'w', encoding="utf-8", newline='') as файл:
#         записчик = csv.writer(файл, delimiter=';')
#         первая_строка_для_цсв = list(взять_данные_из_товара(список_товаров[0]).keys())
#         записчик.writerow(первая_строка_для_цсв)
#
#         for товар in список_товаров:
#             данные_товара = взять_данные_из_товара(товар)
#             значения = []
#             for значение in данные_товара.values():
#                 значения.append(значение)
#             if значения:
#                 записчик.writerow(значения)


# def добавить_товары_в_глав_список(итог):
#     print("Добавление товара в главный список", len(список_товаров))
#     список_товаров.append(итог)


def получить_товары_по_городам():
    print("Количество городов:", len(список_кодов_товаров))

    i = -1
    for код_города in список_кодов_товаров:
        i += 1

        начальное_время = time.time()

        коды_товаров = список_кодов_товаров[код_города]
        # коды_товаров = [(код_города, код_товара) for код_товара in коды_товаров]

        # https://www.youtube.com/watch?v=LddlE3n00W8&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=8 про map_async
        with multiprocessing.Pool(multiprocessing.cpu_count() * УМНОЖИТЕЛЬ_ПРОЦЕССОВ) as p:
            for код_товара in коды_товаров:
                p.apply_async(получить_данные_на_товар, args=(код_города, код_товара), callback=записать_товар_в_цсв)

            p.close()
            p.join()

        # pool = multiprocessing.Pool(multiprocessing.cpu_count() * 2)
        # итог = pool.map(получить_данные_на_товар, коды_товаров)
        # список_товаров.extend(итог)

        print("--- %s секунд Загрузка данных товаров одного города---" % (time.time() - начальное_время))

        # записать_товары(код_города)

        if i == 1:
            break  # количество обрабатываемых городов


основные_ключи = ['название', 'изы', 'главная иза', 'категории', 'вес', 'высота', 'длина', 'ширина', 'цена1', 'цена2',
                  'цена3', 'цена4', 'количество', 'описание', 'ссылка']
ключи_дополнительные = []
CSV = 'petrovich'
файл = None
записчик = None
tek_gorod = ''


def записать_товар_в_цсв(ключи_словарь_код_города):
    ключи_словарь = ключи_словарь_код_города[0]
    код_города = ключи_словарь_код_города[1]

    print(ключи_словарь)

    global основные_ключи
    global ключи_дополнительные
    global файл
    global счётчик_товаров
    global записчик
    global tek_gorod

    значения = []
    # 1
    if 'title' in ключи_словарь and ключи_словарь['title']:
        значения.append(ключи_словарь['title'])
    else:
        значения.append('')

    # 2
    if 'images' in ключи_словарь and ключи_словарь['images']:
        значения.append(ключи_словарь['images'])
    else:
        значения.append('')

    # 3
    if 'cover_image' in ключи_словарь and ключи_словарь['cover_image']:
        значения.append(ключи_словарь['cover_image'])
    else:
        значения.append('')

    # 4
    if 'breadcrumbs' in ключи_словарь and ключи_словарь['breadcrumbs']:
        категории = []
        for категория in ключи_словарь['breadcrumbs']:
            категории.append(категория['title'])
        значения.append(категории)  # категории
    else:
        значения.append('')

    # 5
    if 'weight' in ключи_словарь and ключи_словарь['weight']:
        значения.append(ключи_словарь['weight'])
    else:
        значения.append('')

    # 6
    if 'height' in ключи_словарь and ключи_словарь['height']:
        значения.append(ключи_словарь['height'])
    else:
        значения.append('')

    # 7
    if 'length' in ключи_словарь and ключи_словарь['length']:
        значения.append(ключи_словарь['length'])
    else:
        значения.append('')

    # 8
    if 'width' in ключи_словарь and ключи_словарь['width']:
        значения.append(ключи_словарь['width'])
    else:
        значения.append('')

    # 9
    if 'price' in ключи_словарь and 'gold' in ключи_словарь['price'] and ключи_словарь['price']['gold']:
        значения.append(ключи_словарь['price']['gold'])
    else:
        значения.append('')

    # 10
    if 'price' in ключи_словарь and 'retail' in ключи_словарь['price'] and ключи_словарь['price']['retail']:
        значения.append(ключи_словарь['price']['retail'])
    else:
        значения.append('')

    # 11
    if 'price' in ключи_словарь and 'points' in ключи_словарь['price'] and ключи_словарь['price']['points']:
        значения.append(ключи_словарь['price']['points'])
    else:
        значения.append('')

    # 12
    if 'price' in ключи_словарь and 'individual' in ключи_словарь['price'] and ключи_словарь['price']['individual']:
        значения.append(ключи_словарь['price']['individual'])
    else:
        значения.append('')

    # 13
    if 'remains' in ключи_словарь and 'supply_ways' in ключи_словарь['remains'] and ключи_словарь['remains']['supply_ways']:
        значения.append(ключи_словарь['remains']['supply_ways'][0]['total'])
    else:
        значения.append('')

    # 14
    if 'description' in ключи_словарь and ключи_словарь['description']:
        значения.append(ключи_словарь['description'])
    else:
        значения.append('')

    # 15
    if 'link' in ключи_словарь and ключи_словарь['link']:
        значения.append(ключи_словарь['link'])
    else:
        значения.append('')

    # характеристики
    if ключи_словарь['properties']:

        # готовим словарь характеристик
        характеристики = {}
        for характеристика in ключи_словарь['properties']:
            характеристики.update({характеристика['title']: характеристика['value'][0]['title']})

        # записываем новые ключи в заголовки
        for ключ_характеристики in характеристики:
            if ключ_характеристики not in ключи_дополнительные:
                ключи_дополнительные.append(ключ_характеристики)

        # записываем значения
        for ключ in ключи_дополнительные:
            if ключ not in характеристики:
                значения.append('')
            else:
                значения.append(характеристики[ключ])
    else:
        значения.append('')

    # Если текущий город изменился, создаём переключаемся на другой файл (по городу)
    if tek_gorod != код_города:
        if файл:
            файл.close()
        файл = open(папка_для_товарных_данных + '/' + CSV + '_' + код_города + '.csv', 'w', newline='',
                    encoding="utf-8")
        записчик = csv.writer(файл, delimiter=';')
        tek_gorod = код_города
    else:
        if файл:
            записчик = csv.writer(файл, delimiter=';')

    # записываем список значений в файл
    записчик.writerow(значения)

    print(счётчик_товаров)
    счётчик_товаров += 1


папка_для_кодов_товаров = r'kody_tovarov'
папка_для_товарных_данных = r'tovary_po_gorodam'

список_кодов_товаров = {}


def вставить_заголовки_во_все_цсв():
    все_цсв_файлы = [f for f in listdir(папка_для_товарных_данных) if isfile(join(папка_для_товарных_данных, f))]

    for файл_цсв in все_цсв_файлы:
        # открываем цсв
        with open(папка_для_товарных_данных + '/' + файл_цсв, 'r', encoding="utf-8") as файл_2:
            # считываем все строки разом в список
            все_строки_из_цсв_файла = list(csv.reader(файл_2, delimiter=";"))

        все_строки_из_цсв_файла.insert(0, основные_ключи)  # вставляем в список заголовки

        # записываем итог
        with open(папка_для_товарных_данных + '/' + файл_цсв, 'w', newline='', encoding="utf-8") as файл_3:
            записчик_2 = csv.writer(файл_3, delimiter=';')

            # записываем сразу все строки разом
            записчик_2.writerows(все_строки_из_цсв_файла)


if __name__ == '__main__':
    # урл_для_проверки_прокси = 'https://api.petrovich.ru/catalog/v2.3/products/500994?city_code=rf&client_id=pet_site'
    # рабочие_прокси = poluchit_spis_godnyh_proxei(урл_для_проверки_прокси, заголовки)
    #
    # if not рабочие_прокси:
    #     print('Нету адресов прокс')
    #     exit()

    if not os.path.exists(папка_для_товарных_данных):
        os.makedirs(папка_для_товарных_данных)

    # количество процессов = умножитель * количество ядер вычислителя
    УМНОЖИТЕЛЬ_ПРОЦЕССОВ = 1

    запрос_к_городам = 'https://api.petrovich.ru/geobase/v1.1/cities?city_code=spb&client_id=pet_site'

    коды_городов = получить_кода_городов(запрос_к_городам)

    категории_по_городам = получить_категории_по_городам(коды_городов)

    получить_список_всех_товаров(категории_по_городам)

    # записать_коды_товаров(список_кодов_товаров)

    получить_товары_по_городам()

    # # записываем заголовок вниз
    # записчик.writerow(ключи)

    if файл:
        файл.close()

    основные_ключи = основные_ключи + ключи_дополнительные

    # записываем ключи в отдельный файл на всякий случай
    with open('petrovich_kluchi.txt', 'w', newline='', encoding="utf-8") as файл_ключей:
        записчик_1 = csv.writer(файл_ключей, delimiter=';')
        записчик_1.writerow(основные_ключи)

    вставить_заголовки_во_все_цсв()
