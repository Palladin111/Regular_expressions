import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

list_new = []
for list in contacts_list:
    str = ' '.join(list[0:3])
    list_1 = str.split(' ')
    list_var = list_1[0:3] + list[3:7]
    list_new.append(list_var)

pattern_phone = re.compile(r"(\+7|8)?\s*\(*(\d\d\d)\)*[-\s]*(\d\d\d)[-\s]*(\d\d)"
                           r"[-\s]*(\d\d\s*)\(*([доб.]*)\s*(\d*)\)*")

list_new_1 = []
list_new_2 = []
for list in list_new:
    for list_1 in list:
        result = pattern_phone.sub(r"+7(\2)\3-\4-\5\6\7", list_1)
        list_new_1.append(result)
    list_new_2.append(list_new_1.copy())
    list_new_1.clear()

dict_end = {}
list_v = []
list_comp = list_new_2.copy()
for list_var in list_new_2:
    if list_var[0] + ' ' + list_var[1] not in dict_end.keys():
        dict_end[list_var[0] + ' ' + list_var[1]] = list_var[2:]
    else:
        i = 0
        for l in dict_end.get(list_var[0] + ' ' + list_var[1]):
            if l == '':
                list_v.append(list_var[i + 2])
            else:
                list_v.append(l)
            i += 1
        dict_end[list_var[0] + ' ' + list_var[1]] = list_v.copy()
        list_v.clear()

list_end = []
for k, v in dict_end.items():
    list_v2 = k.split(' ')
    list_v2.extend(v)
    list_end.append(list_v2)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(list_end)