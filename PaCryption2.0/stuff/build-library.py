import secrets

abcA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z", " ", "."]
abcS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ  ."
file = open("library.txt", "w", encoding="utf-8")
a = []
list_cache = []
signs = "!'§$%&/()=?*+#"
l = []
nZ = 0
while nZ <= 378:
    cache = []
    a = []
    nZ += 1
    for element in signs:
        l = [element]
        for i in range(2):
            random = ""
            while True:
                random = secrets.choice(abcS)
                if random not in cache:
                    break
            l.append(random)
            cache.append(random)
        a.append(l)
    ident = False
    for aList in list_cache:
        if a == aList:
            ident = True
            break
    if ident is True:
        continue
    list_cache.append(a)
    file.write(str(a) + ",\n")
    print(str(a))

file.flush()
file.close()
