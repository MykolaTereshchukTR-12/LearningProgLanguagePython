Laboratory work #3.

In this laboratory work, it was necessary to select a pair of numbers whose sum is equal to 10. 

The numbers themselves are entered through the input() function.

For the program to work properly, you need to enter the size of your array (the number of numbers) that the program will process. 

Then enter your numbers in order.

The code looks like this:

```python
def findten(l): #Функція для пошуку пари чисел, сума яких дає 10
    Lpary = [] #Створюємо масив для розміщення пари, сума яких дасть 10
    for i in l: #Цикл пройде всі числа масиву
        lcopy = l[:] #Створюємо копію оригінального масиву для запобігання його зміни
        lcopy.remove(i) #Видаляємо елемент і для запобігання його повторної фіксації 
        for j in lcopy: #Тепер пробігаємо по числах скопійованого масиву
            if i + j == 10: #Шукаємо пару чисел, сума яких рівна 10
                if [i, j] in Lpary or [j, i] in Lpary: #Даний умовний оператор перевіряє наявність однакових пари
                    pass #Даний оператор пропускає ітерацію циклу
                else:
                    Lpary.append([i, j]) #Додаємо пару чисел у масив для зберігнання пар
                    print(i, "+", j, "= 10") #Виведення пари
                
#Main block
L = [] #Створюємо пустий масив для запису введених чисел
for i in range(int(input("Input size of list: "))): #Спочатку ми вводимо розмір масиву, конвертуємо у тип int і виконуємо цикл відповідно до значення розміру масиву
    L.append(int(input("Input numbers: "))) #Окремо вводимо числа масиву
findten(L) #Звертаємось до функції findten, котра буде шукати пари чисел, сума яких дає 10
```

Some examples of code:

![Example1][Example1]

![Example2][Example2]

![Example3][Example3]

[Example1]: https://github.com/MykolaTereshchukTR-12/LearningProgLanguagePython/edit/MaiNBrancH/Laboratory%20work%203.%20Find%20sume%2010/Example1.jpg
[Example2]: https://github.com/MykolaTereshchukTR-12/LearningProgLanguagePython/edit/MaiNBrancH/Laboratory%20work%203.%20Find%20sume%2010/Example2.jpg
[Example3]: https://github.com/MykolaTereshchukTR-12/LearningProgLanguagePython/edit/MaiNBrancH/Laboratory%20work%203.%20Find%20sume%2010/Example3.jpg
