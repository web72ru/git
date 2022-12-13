import time
import random
# Уровней здания
urovni = list(range(9))

# Вызовы с уровней
vyzovy_vverh = [8, 5]
vyzovy_vverh.sort()
vyzovy_vniz = [1, 4]
vyzovy_vniz.sort(reverse = True)

# Вызовы из подъемника
vyzov_iz_podyemnika = []

# Производство случайных вызовов
def sozdat_vyzov():
    sluchaynoe_chislo = random.choice(urovni)
    sluchayny_vyzov = sluchaynoe_chislo
    return sluchayny_vyzov

# Нахождение подъёмника
tek_uroven = 10

# Направление
napravlenie = True

# Сообщения
opisanie = ["↑", "↓", "Едем на:", "Текущий:", "Очередь:", "Остановка на:", "Выбран уровень:", "Двери закрываются", "--------------------------------", "Загрузка/Выгрузка пассажиров", "Очередь:"]

# Задержка.
def zaderzhka():
    time.sleep(1)

# Остановка
def ostanovka():
    
    # Вызов из подъёмника
    vyzov_iz_podyemnika.append(6)
    print(random.seed())
    # Описание остановки
    print(opisanie[8]) # Черта
    print(opisanie[5], tek_uroven) # Текущий уровень

    # Перенос вызовов с временного списка в постоянные
    for vyzov in vyzov_iz_podyemnika:
        if tek_uroven < vyzov:
            vyzovy_vverh.append(vyzov)

        elif tek_uroven > vyzov:
            vyzovy_vniz.append(vyzov)

        else:
            break

    # Удаление повторов
    list(set(vyzovy_vverh))
    list(set(vyzovy_vniz))

    # Сортировка
    vyzovy_vverh.sort()
    vyzovy_vniz.sort(reverse=True)

    if napravlenie == True:
        vyzovy_vverh.remove(vyzovy_vverh[0]) # Удаление пройденного вызова в списке вверх
        print(opisanie[10], vyzovy_vverh) # Очередь вверх
    elif napravlenie == False:
        vyzovy_vniz.remove(vyzovy_vniz[0]) # Удаление пройденного вызова в списке вниз
        print(opisanie[10], vyzovy_vniz) # Очередь вниз

    print(opisanie[6], vyzov_iz_podyemnika)  # Вызов из подъёмника
    
    # Очистка временного списка
    vyzov_iz_podyemnika.clear()

    print(opisanie[8]) # Черта
    time.sleep(3)

# Описание движения
def dvizhenie():
    if napravlenie == True:
        print(opisanie[0], opisanie[2], vyzovy_vverh[0], opisanie[3], tek_uroven, opisanie[10], vyzovy_vverh)
    elif napravlenie == False:
        print(opisanie[1], opisanie[2], vyzovy_vniz[0], opisanie[3], tek_uroven, opisanie[10], vyzovy_vniz)


# =====================================================================

# Работа подъемника
petlya = True
while petlya:
    zaderzhka()
    if vyzovy_vverh != [] and tek_uroven == vyzovy_vverh[0]:
        ostanovka()

    elif vyzovy_vverh != [] and  tek_uroven < vyzovy_vverh[0]:
        tek_uroven += 1
        dvizhenie()
        if tek_uroven in vyzovy_vverh:
            for vyzov in vyzovy_vverh:
                if vyzov > tek_uroven:
                    ostanovka()

    elif vyzovy_vniz != [] and tek_uroven == vyzovy_vniz[0]:
        ostanovka()

    elif vyzovy_vniz != [] and tek_uroven > vyzovy_vniz[0]:
        napravlenie = False
        tek_uroven -= 1
        dvizhenie()
        if tek_uroven in vyzovy_vniz:
            for vyzov in vyzovy_vniz:
                if vyzov < tek_uroven:
                    ostanovka()

    else:
        print("Стоим")
        break