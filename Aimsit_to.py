alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
smeshenie = int(input('Шаг шифровки: '))
message = input("Сообщение для шифровки: ").upper()
itog = ''
lang = input('Выберите язык RU/EU: ')   #Добавляем возможность выбора языка
if lang == 'RU':
    for i in message:
        mesto = alfavit_RU.find(i)   # Алгоритм для шифрования сообщения на русском 
        new_mesto = mesto + smeshenie
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        else:
            itog += i
else:
    for i in message:
        mesto = alfavit_EU.find(i)		# Алгоритм для шифрования сообщения на английском 
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
