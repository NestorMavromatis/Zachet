Line=input(" "). split()
cnt = 0
for i, s in enumerate(Line):
    if s.isdigit():
        cnt+= len(s)
if cnt == 0:
    print("Нема цифор")
else:
    print("", cnt)
 """ Вводим строку произольной длины, прога выводит кол-во цифр в этой строке (с помощью сплита разбиваем строку, ставим 
 счётчик на ноль, а дальше считаем кол-во цифр по разбитым элементам. 
 Если их нет, то выводится соответсвующее сообщение"""
def Len (s):
    if type (s) != str:
        raise TypeError ('Expected str, got {}'.format(type(s)) )

    return s[: : -1]