#Polindrom
# word = "дед дед"
# word = word.lower()


# def palindrom(word):
#     if len(word) == 1 or len(word) == 0:
#         return 0 
#     if word[0] == word[-1]:
#         return palindrom(word[1:-1])
#     else:
#        return 1 

# test = palindrom(word)
# if test == 0:
#     print("Yes")
# elif test == 1:
#     print("No")

#Dvoichn
# number = int(input('Input Nuber  '))
# b = ''
 
# while number > 0:
#     b = str(number % 2) + b
#     number = number // 2
 
# print(b)

#Desyat
# def desiat(digit):
#     long= len(digit)
#     desiat_number = 0
#     for i in range(0, long):
#         desiat_number = desiat_number+int(digit[i])*(2**(long-i-1))
#     return desiat_number
# a = input('Input number')
# print(desiat(a))

#Stepen
# def pow(base, exp):
#     if (exp == 1):
#         return (base)
#     if (exp != 1):
#         return (base * pow(base, exp - 1))
# base = int(input("Введите число: "))
# exp = int(input("Введите его степень: "))
# print("Результат возведения равен:", pow(base, exp))

#Sum list
# list_num = [1, 2, 3]
# Sum = 0
 
# def Sum_list(x):  
#     global Sum
#     if x == len(list_num):
#         return    
#     Sum  += list_num[x]
#     Sum_list(x+1)
 
# Sum_list(0)
# print(Sum)

#Proverka prostogo chisla
# a = int(input("Input number: "))
# k = 0
# for i in range(2, a // 2+1):
#     if (a % i == 0):
#         k = k+1
# if (k <= 0):
#     print("YES")
# else:
#     print("NO")