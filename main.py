stroka1 = str(input("введите первую строку ")) #запрос для того,чтобы ввести строку
stroka2 = str(input("введие вторую строку "))
strok1 = sorted(stroka1.lower()) #сортировка строки и преобразование в нижний регистр 
strok2 = sorted(stroka2.lower())
if strok1 == strok2: #условие 
    print(f"{stroka1} и {stroka2} являются анаграммами") #вывод результата
else:
    print(f"{stroka1} и {stroka2} не являются анаграммами")