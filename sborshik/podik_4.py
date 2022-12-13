import time
import random
# Уровней здания
urovni = list(range(9))

# Вызовы с уровней
vyzovy_vverh = [2, 5, 8]
vyzovy_vverh.sort()
vyzovy_vniz = [5, 7, 3]
vyzovy_vniz.sort(reverse = True)

# Вызовы из подъемника
vyzov_iz_podyemnika = []

# Производство случайных вызовов
def sozdat_vyzov():
    sluchaynoe_chislo = random.choice(urovni)
    sluchayny_vyzov = sluchaynoe_chislo
    return sluchayny_vyzov

# Нахождение подъёмника
tek_uroven = 0

# Направление
napravlenie = True

# Сообщения
opisanie = ["↑", "↓", "Едем на:", "Текущий:", "Очередь:", "Остановка на:", "Вызов из подъёмника:", "Двери закрываются", "--------------------------------", "Загрузка/Выгрузка пассажиров", "Следующие остановки:"]

# Задержка.
def zaderzhka():
    time.sleep(1)

# Описание остановки
def ostanovka():

    # Описание остановки
    print(opisanie[8])
    print(opisanie[5], tek_uroven)

    # Вызов из подъёмника
    vyzov_iz_podyemnika.append(sozdat_vyzov())

    if tek_uroven < vyzov_iz_podyemnika[0]:
        for vyzov in vyzov_iz_podyemnika:
            if vyzov_iz_podyemnika in vyzovy_vverh:
                del vyzov_iz_podyemnika[vyzov]
            else:
                vyzovy_vverh.append(vyzov)
                vyzovy_vverh.sort()
            print(opisanie[6], vyzov_iz_podyemnika)
            vyzov_iz_podyemnika.remove(vyzov)

    elif tek_uroven > vyzov_iz_podyemnika[0]:
        for vyzov in vyzov_iz_podyemnika:
            if vyzov_iz_podyemnika in vyzovy_vniz:
                del vyzov_iz_podyemnika[vyzov]
            else:
                vyzovy_vniz.append(vyzov)
                vyzovy_vniz.sort(reverse = True)

            print(opisanie[6], vyzov_iz_podyemnika)
            vyzov_iz_podyemnika.remove(vyzov)

    else:
        vyzov_iz_podyemnika.remove(vyzov_iz_podyemnika[-1])

    # Удаление пройденых остановок
    if napravlenie == True:
        vyzovy_vverh.remove(vyzovy_vverh[0])
    elif napravlenie == False:
        vyzovy_vniz.remove(vyzovy_vniz[0])

    print(opisanie[8])
    time.sleep(3)

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
    if vyzovy_vverh != [] and tek_uroven == vyzovy_vverh[0] and len(vyzovy_vverh) == 1:
        ostanovka()

    elif vyzovy_vverh != [] and  tek_uroven < vyzovy_vverh[0]:
        tek_uroven += 1
        dvizhenie()
        if tek_uroven in vyzovy_vverh:
            for vyzov in vyzovy_vverh:
                if vyzov > tek_uroven:
                    ostanovka()

    elif vyzovy_vniz != [] and tek_uroven == vyzovy_vniz[0] and len(vyzovy_vniz) == 1:
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