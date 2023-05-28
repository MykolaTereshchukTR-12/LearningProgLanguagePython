Лабораторна робота №4: Аналіз файлів

Основне завдання лабораторної роботи: написати програму, яка надає статистику щодо заданого файлу: 
1. Кількість рядків; 
2. Кількість порожніх рядків; 
3. Кількість рядків з літерою "z"; 
4. Кількість літер “z” у файлі; 
5. Кількість рядків з групою символів “and” (наприклад, "andromeda" містить "and" так само, як і "you and me"). 

Програма повинна містити наступне:
Запит на отримання шляху до файла;
Запит на аналіз наступного файлу;
Запит на продовження роботи самої програми з можливим її завершенням. 

Код програми виглядає наступним чином:


```python
def MAINNN(): #Створимо керуючу функцію, яка буде працювати залежно від введеного параметра
    print("Do you want to continue? (Use \"Yes\" to continue and \"No\" to close the application)")
    l = input() 
    if l == "Yes": #Якщо користувач бажає дослідити файл
        print("GOOOD! =)")
        ANALYZEYOURFILE() #Викликаємо основну функцію, яка досліджувати файл
    else: #Дії при негативній відповіді
        print("Bye!") 
        exit() #Вихід з програми

def ANALYZEYOURFILE(): #Досліджуюча функція 
    print("Enter the path to the file you want to examine based on the sample (Disk:\\...\\...\\file_name.txt): ")
    Locate = input() #Створення змінної, яка зберігатиме шлях до файлу
    with open(Locate, "r") as fILE: #Дана строка коду дозволяє правильно відкрити файл для читання, а також
    #правильно закрити навіть у випадку виникнення помилки 
        number_of_lines = fILE.readlines() #Створення об'єкту, який зберігатиме вміст текстового файлу у вигляді списку рядків
        all_of_z = 0 #Змінна для збереження кількості літер "z"
        all_of_null_line = 0 #Змінна для збереження кількості пустих рядків
        all_lines_of_and = 0 #Змінна для збереження кількості рядків з групою символів "and"
        all_lines_of_z = 0 #Змінна для збереження кількості рядків з літерами "z"
        for line in number_of_lines: #Створення циклу, яких буде досліджувати кожний елемент (рядок) списку рядків файлу
            all_of_z += line.count("z") #Сумування всіх наявних літер "z" у рядку
            if line == "\n": #Якщо рядок виявився пустим
                all_of_null_line += 1 
            if (line.find('and')) != -1: #Якщо в рядку виявилась група символів "and"
                all_lines_of_and += 1 
            if (line.find('z')) != -1: #Якщо в рядку наявна літера "z"
                all_lines_of_z += 1
        print(number_of_lines, "\n\n>>>\n")
        print("File: ", Locate, "\nTotal lines: ", len(number_of_lines))
        print("Empty lines: ", all_of_null_line, "\nLines with \"z\": ", all_lines_of_z) #Виведення результатів
        print("\"z\" count: ", all_of_z, "\nLines with \"and\": ", all_lines_of_and)
    MAINNN() #Повернення до функції керування

print("Hi! Let's analuze your files!")
MAINNN() #Початок роботи
```

Приклад результату програми:

![Exampl1](https://github.com/MykolaTereshchukTR-12/LearningProgLanguagePython/blob/MaiNBrancH/Laboratory%20work%204.%20Analyze%20files/Lab_4_Photo_of_example.jpg)
