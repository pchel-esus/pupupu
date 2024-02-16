import csv

#считывание данных
f = open('scientist.csv',encoding='utf-8')
ans = list(csv.reader(f,delimiter=',',quotechar='"'))[1:]
f.close()

#поиск кол-ва изобретений в каждом месяце
d = {}
dates = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
for i in ans:
    date = int(i[-2].split('-')[1]) - 1
    if dates[date] not in d:
        d[dates[date]] = 1
    else:
        d[dates[date]] += 1

#запись данных в файл
f_write = open('scientist_new.csv','w',encoding='utf-8')
f_write.write('month, count\n')
for i in d:
    f_write.write(f'{i}, {d[i]}\n')
f_write.close()

#вывод месяца с наибольшим кол-вом препаратов
m = 0
m_name = ''
for i in d:
    if d[i] > m:
        m = d[i]
        m_name = i

print(f'{m_name} наиболее благоприятен для ученых. В этом месяце было создано - {m} препарат(-а)')