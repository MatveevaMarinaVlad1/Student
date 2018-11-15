import random

# цифры (обучающая выборка)

num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001010100111')
num3 = list('111001011001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# виды цифры 5(test)

num51 = list('111100111000111')
num52 = list('111100010001111')
num53 = list('111100011001111')
num54 = list('110100111001111')
num55 = list('110100111001011')
num56 = list('111100101001111')

# инициализация весов сети
# weights = [0 for i in range(15)]

weights = []
for i in range(15):
    weights.append(0)

# порог функции активации

bias = 7

# является ли данное число 5

def proceed(number):
    # взвешанная сумма
    net = 0
    for i in range(15):
        net += weights[i]*int(number[i])
    # превышен ли порог? (да - сеть думает, что это 5, нет - другая цифра)
    return net>=bias
    '''if (net>=bias):
        return True
    else
        return False'''
#уменьшение значений весов, если сеть ошиблась и выдала 1
def decrease(number):
    for i in range(15):
        if (int(number[i])==1):
            weights[i] -=1

            
#увеличение значений весов, если сеть ошиблась и выдала 0
def increase(number):
    for i in range(15):
        if (int(number[i])==1):
            weights[i] +=1    

# тренировка сети

for i in range(10000):
    option = random.randint(0,9)

    if (option!=5):
        if (proceed(nums[option])):
            decrease(nums[option])
    else:
        if not proceed(num5):
            increase(num5)
# вывод результатов
print(weights)
#прогон по тестовой выборке
print ("0 это число 5?", proceed(num0))
print ("1 это число 5?", proceed(num1))
print ("2 это число 5?", proceed(num2))
print ("3 это число 5?", proceed(num3))
print ("4 это число 5?", proceed(num4))
print ("6 это число 5?", proceed(num6))
print ("7 это число 5?", proceed(num7))
print ("8 это число 5?", proceed(num8))
print ("9 это число 5?", proceed(num9), "\n")
            
# прогон по обучающей выборке
print ("5 - 5?", proceed(num5))
print ("5 - искаженная 5.1?", proceed(num51))       
print ("5 - искаженная 5.2?", proceed(num52))
print ("5 - искаженная 5.3?", proceed(num53))
print ("5 - искаженная 5.4?", proceed(num54))
print ("5 - искаженная 5.5?", proceed(num55))
print ("5 - искаженная 5.6?", proceed(num56))




