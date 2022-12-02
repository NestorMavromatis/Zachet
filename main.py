Line=input(" "). split()
cnt = 0
for i, s in enumerate(line):
    if s.isdigit():
        cnt+= len(s)
if cnt == 0:
    print("Нема цифор")
else:
    print("", "от стока цифор", cnt)
