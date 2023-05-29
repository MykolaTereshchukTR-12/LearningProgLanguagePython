import math #Підключаємо модуль "Math" для використання функції взяття кореня з числа sqrt()

class CI_mark: #Створення класу, який містить функції для обрахунку відповідних значень
    def E_task(a, m, b): #Функція для обчислення серенього зваженого одного завдання
        return (a + 4 * m + b) / 6
    
    def SD_task(a, b): #Функція для обчислення стандартного відхилення у вигляді L-оцінювача
        return ((b - a) / 6 ) ** 2

    def CI_min_mark(E_sum, SD_sum): #Функція для знаходження нижньої межі 95% довірчого інтервалу 
        return E_sum - 2 * math.sqrt(SD_sum)

    def CI_max_mark(E_sum, SD_sum): #Функція для знаходження верхньої межі 95% довірчого інтервалу
        return E_sum + 2 * math.sqrt(SD_sum)
    
def MAIN(): #Основна функція для отримання відповідних параметрів для оцінювання
    E_project = 0 #Значення середнього зваженого для всього проекту з n завдань
    SD_project = 0 #Значення стандартного відхилення для всього проекту
    for i in range(int(input("Please enter the number of your tasks: "))): #Створення циклу, який знаходить оцінку для n завдань, де n=range(int(input("Please enter the number of your tasks: ")))
        a = int(input("Enter number \"a\": ")) #Отримання найоптимальнішої оцінки
        m = int(input("Enter number \"m\": ")) #Отримання найбільш ймовірної оцінки
        b = int(input("Enter number \"b\": ")) #Отримання найгіршої оцінки
        E_project += CI_mark.E_task(a, m, b) #Знаходження сумарного середнього зваженого 
        SD_project += CI_mark.SD_task(a, b) #Знаходження стандартного відхилення проекту
    print("Project's 95\"%\" confidence interval: ", round(CI_mark.CI_min_mark(E_project, SD_project)), 
        " ... ", round(CI_mark.CI_max_mark(E_project, SD_project)), " points.") #Виведення всіх значень з попереднім заокругленням меж довірчого інтервалу

#Старт програми    
print("Hi! Let`s find 95% confidence interval!")
MAIN() 
while True: #Даний цикл був доданий виключно з вподобань автора
    print("Do you want to continue? (Use \"Yes\" to continue and \"No\" to close the application)")
    l = input() 
    if l == "Yes": #Якщо користувач бажає дослідити файл
        print("GOOOD! =)")
        MAIN() #Викликаємо основну функцію MAIN
    else: #Дії при негативній відповіді
        print("Bye!") 
        exit() #Вихід з програми