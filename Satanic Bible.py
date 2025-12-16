cycle = True
count = 0
count2 = 0
print("=" * 60)
print("ПРОГРАММА 'КАЛЬКУЛЯТ0Р'")
print("=" * 60)
while cycle:
    count2 += 1
    print("Введите первое число")
    chislo1 = int(input())
    print("Что вы хотите сделать : ?Выберите либо первое либо второе.(1/2)")
    print("1)операции с числом")
    print("2)анализ числа")
    otvet1 = input()
    if otvet1 == "1":
        print("Выберите одну из операций:")
        print("1)сложениие")
        print("2)вычитание")
        print("3)умножение")
        print("4)деление")
        print("5)целочисленное деление")
        print("6)взятие остатка")
        print("7)возведение в степень")
        print("8)квадратный корень числа")
        print("9)кубический корень числа")
        print("10)перевод из любой системы счисления в десятичную")
        deistvia = input()
        if deistvia == "1": #сложение
            print("Введите второе число")
            chislo2 = int(input())
            result = chislo1 + chislo2
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!")
        elif deistvia == "2": #вычитание
            print("Введите второе число")
            chislo2 = int(input())
            result = chislo1 - chislo2
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!")
        elif deistvia == "3": #умножение
            print("Введите второе число")
            chislo2 = int(input())
            result = chislo1 * chislo2
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!")     
        elif deistvia == "4": #деление
            print("Введите второе число")
            chislo2 = int(input())
            result = chislo1 / chislo2
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!")         
        elif deistvia == "5": #целочисленное деление
            print("Введите второе число")
            chislo2 = int(input())
            result = chislo1 // chislo2
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!") 
        elif deistvia == "6": #взятие остатка
            print("Введите второе число")
            chislo2 = int(input())
            result = chislo1 % chislo2
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!")                                                                                   
        elif deistvia == "7": #возведение в степень
            print("Введите второе число")
            chislo2 = int(input())
            result = chislo1 ** chislo2
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!")  
        elif deistvia == "8": #квадратный корень
            print("Введите второе число")
            result = chislo1 ** 0.5
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!")      
        elif deistvia == "9": #кубический корень
            print("Введите второе число")
            result = chislo1 ** 1 / 3
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!")                                      
        elif deistvia == "10": #привод
            print("Введите основание системы счисления первого числа")
            chislo3 = str(chislo1)
            osnovanie = int(input())
            result = int(chislo3, base=osnovanie) 
            print(f"Ваш ответ : {result}")
            print("Хотите продолжить?(да/нет)")
            while True:
                count += 1
                dalshe = input()
                if dalshe == "да":
                    cycle = True
                    break
                elif dalshe == "нет":
                    cycle = False
                    break
                else:
                    print("Введите корректный ответ!")   
counter = count - count2
if counter == 0:
    print("Вы большой молодец!!! Спасибо что не дурачились!")
elif counter > 0 and (counter < 10 or counter == 10):
    print("Хз")
elif counter > 10 and (counter < 20 or counter == 20):
    print("Вы можете лучше! Я верю в Вас!!!")
elif counter > 20:
    print("Ответственно заявляю, Вы - негодяй!!!Я даже запишу это.")
    negoday = True
    polsovatel = negoday