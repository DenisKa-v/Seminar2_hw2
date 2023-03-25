stih = 'пара-ра-рам рам-пам-папам па-ра-па-да'
stih2 = stih.split()
# а,у,о,ы,э,я,ю,ё,и,е
stih3 = []
for i in range(len(stih2)):
    stih3.append(stih2[i].count('а'))
stih4 = list(map(lambda x: x % 2 == 0, stih3))
print(stih,'\n', stih2,'\n', stih3, stih4, sep= '')
print(len(stih4))
print(sum(stih4))
if len(stih4) == sum(stih4):
    print('Парам пам-пам')
else:
    print('Пам парам')