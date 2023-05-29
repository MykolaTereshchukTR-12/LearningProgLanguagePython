from num2word import word #Імпортуємо з модуля num2word об'єкт word
print("Hi, my dear friends! Let`s beging!")

def number_to_word(): #Створення функції перетворення числа в слово 
    number = input("Please, enter your number: ")
    print("Your number is: ", word(number))
    infinity() 

def infinity(): #Дана функція створена з вподобань автора для постійної роботи з можливістю виходу з програми
    print("Do you want to continue? (Use \"Yes\" to continue and \"No\" to close the application)")
    l = input() 
    if l == "Yes": #Якщо користувач бажає дослідити файл
        print("GOOOD! =)")
        number_to_word() #Викликаємо основну функцію, яка досліджувати файл
    else: #Дії при негативній відповіді
        print("Bye!") 
        exit() #Вихід з програми

number_to_word()