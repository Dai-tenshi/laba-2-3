def romeNumber(x):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM","MMM","MMMM"]

    t = thous[x // 1000]
    h = hunds[x // 100 % 10]
    te = tens[x // 10 % 10]
    o =  ones[x % 10]
    return t+h+te+o


import time
digit = 0
tempNum = ""
more_max_buffer_len = False    # максимальный размер рабочего буфера
max_buffer_len = 100    # максимальный размер рабочего буфера
buffer_len = 1         # размер буфера чтения
work_buffer = []                # рабочий буфер
digit_flag = False              # флаг наличия цифры
number_flag = False
try:
    print("\n-----Результат работы программы-----\n -----Локальное время",time.ctime(),"-----")
    start = time.time()       
    with open("test1.txt", "r") as file:         # открываем файл
        buffer = file.read(buffer_len)          # читаем первый блок
        if not buffer:                          # если файл пустой
            print ("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
            
        while buffer:                               # пока файл не пустой
            while (buffer<'0' or buffer>'9') and buffer:         # ищем цифры
                buffer = file.read(buffer_len)      # читаем очередной блок
                if buffer.isnumeric() != True:      ##если символ(буква) то останавливаем программу
                    print("работа программы только с целыми числами, отредоктируйте файл и повторите попытку заново")
                    break
            while buffer:  #обрабатываем цифры
               ##другого способа работы с посимвольным чтением не нашёл так что вот
                if buffer.isnumeric() == True:    ##если цифра то начинаем посимвольно записывать в массив и после это дело конвертировать
                    number_flag = True
                    tempNum += buffer
                else:
                    number_flag = False
                    work_buffer.append(tempNum)
                    tempNum = ""
                if len(work_buffer) >= max_buffer_len and buffer :    # Если буфер переполнен и в нем нет цифр
                    print ("\nФайл text.txt содержит блок цифр, превышающий максимальный размер буфера = "+str(max_buffer_len)+ " символов.\nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
                    more_max_buffer_len = True
                buffer = file.read(buffer_len)  # читаем очередной блок
            if more_max_buffer_len:
                break
        if not digit_flag and number_flag:                  # печатем число
                print (work_buffer,' ')            
                digit_flag = False
                number_flag = False
        ##вызываем саму функцию
        numInt = [int(x) for x in work_buffer]       
        for x in range(len(numInt)):
            print(romeNumber(numInt[x]))
        finish = time.time()
        result = finish - start
        print("Program time: " + str(result) + " seconds.")        
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.") 
    
