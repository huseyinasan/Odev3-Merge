bolunenler = []

for i in range(100):
    if(i%3 != 0):
        continue
    else:
        bolunenler.append(i)
print(bolunenler)
print(len(bolunenler))