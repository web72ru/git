import time
import random

# Количество уровней в доме
urovni = list(range(10))

# Нахождение подъёмника
tek_uroven = 0

# Вызов подъёмника вверх.
vyzovy = [[urovni[9], False], [urovni[8], False], [urovni[2], True], [urovni[5], True]]

# vyzovy_false - вызовы вниз. vyzovy_true - вызовы наверх
vyzovy_false = []
vyzovy_true = []


# Задержка.
def zaderzhka():
    time.sleep(1)


# Сообщение о прибытии для vyzovy_false
def pribytie_vyzovy_false():
    if tek_uroven == max(vyzovy_false) or tek_uroven in vyzovy_true:
        print("--------------------------------")
        print(f"{tek_uroven} уровень.")
        print("--------------------------------")
        time.sleep(4)


# Сообщение о прибытии для vyzovy_true
def pribytie_vyzovy_true():
    if tek_uroven == min(vyzovy_true) or tek_uroven in vyzovy_false:
        print("--------------------------------")
        print(f"{tek_uroven} уровень.")
        print("--------------------------------")
        time.sleep(4)


# Описание движения подъемника
def vverh():
    print(f"Направление: ↑ на {max(vyzovy_false)} уровень. Текущий: {tek_uroven}. {vyzovy_false} {vyzovy_true}")


def vniz():
    print(f"Направление: ↓ на {min(vyzovy_true)} уровень. Текущий: {tek_uroven}. {vyzovy_false} {vyzovy_true}")


# Производство случайного вызова
def sozdat_vyzov():
    sluchay_chislo = random.choice(urovni)
    sluchay_bool = bool(random.getrandbits(1))
    sluchay_vyzov = list([sluchay_chislo, sluchay_bool])
    return sluchay_vyzov


# Работа подъемника
petlya = True
while petlya:
    # Разделение вызовов по направлениям ↑ или ↓
    for vyzov in vyzovy:
        if vyzov[1] == False:
            vyzovy_false.append(vyzov[0])  # добавляем в список vyzovy_false

        elif vyzov[1] == True:
            vyzovy_true.append(vyzov[0])  # добавляем в список vyzovy_true
    vyzovy = []

    zaderzhka()

    if vyzovy_false != [] and tek_uroven < max(vyzovy_false):
        tek_uroven += 1
        vverh()  # описание движения вверх
        pribytie_vyzovy_false()  # прибытие

        if tek_uroven in vyzovy_false and tek_uroven >= max(vyzovy_false):
            vyzovy_false.remove(tek_uroven)  # удаляем из списка vyzovy_false
            # vyzovy.append([urovni[1], True]) # добавляем в список vyzovy

    elif vyzovy_true != [] and tek_uroven > min(vyzovy_true):
        tek_uroven -= 1
        vniz()  # описание движения вниз
        pribytie_vyzovy_true()  # прибытие

        if tek_uroven in vyzovy_true and tek_uroven <= min(vyzovy_true):
            vyzovy_true.remove(tek_uroven)  # удаляем из списка vyzovy_true
            # vyzovy.append([urovni[8], False]) # добавляем в список vyzovy
    else:
        print("Стоим")
        break