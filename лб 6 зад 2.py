A=[[1,-1,3],
   [-9,5,-4],
   [5,7,4],
   [-2,-7,-5]]#вводим список и его значения
def zamena_minusovix(a):#определяем функцию zamena_minusovix(a)
    for i in range(len(a)):#проводим итерацию по элементам списка
        for j in range(len(a[i])):#проводим итерацию по элементам внутреннего списка
            if a[i][j]<0:#проверяем является ли число минусовым
                a[i][j]=-a[i][j]#если число является минусовым то щ=зяменяем его на положительное число
    return a#возвращяемя к а
res=zamena_minusovix(A)#вводим результат который равен функции замены переменных в списке
print(res)#выводим результат