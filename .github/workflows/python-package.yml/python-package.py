Задания, необходимо написать код:
1. Составить алгоритм: если введенное число больше 7, то вывести “Привет”.
# создадим числа
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# создадим функцию, в которой, если число больше 7, то на экран выводит "Привет".
def right_numbers(numbers):
    if numbers > 7:
        print("Привет")
right_numbers(10)

2. Составить алгоритм: если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”, если нет, то вывести "Нет такого имени".
# создадим имена
word = ["Александр", "Вячеслав", "Константин"]
# создадим функцию если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”, если нет, то вывести "Нет такого имени".
def right_name(word):
    if word == "Вячеслав":
        print("Привет, Вячеслав")
    else:
        print("Нет такого имени")
right_name("Вячеслав")

3. Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3.
# возьмем числа от 1 до 100, выведем значения кратны трём
print([i for i in range(1,100) if i%3==0])

4. Дана скобочная последовательность: [((())()(())]]
- Можно ли считать эту последовательность правильной?
- Если ответ на предыдущий вопрос “нет” - то что необходимо в ней изменить, чтоб она стала правильной?
Ответ:
Нет. Скобочная последовательность неправильная. Если массив открывается, то и должен закрываться, если скобка открывается, то должна закрываться.
Примеры: [()()()], [(()())()], [(()()())], [()(()())].
