list_Name = ['Kevin', 'Jalon', 'Miya', 'Nana']
list_English = [99, 80, 88, 95]
list_Chines = [90, 100, 95, 88]
list_mathematics = [100, 93, 94, 98]
list_Chines[0] + list_mathematics[0] + list_English[0]
list_Chines[1] + list_mathematics[1] + list_English[1]
for t in range(len(list_Name)):
    total = list_Chines[t] + list_mathematics[t] + list_English[t]
    print('%s的总成绩是：%s + %s + %s = %s' % (list_Name[t], list_Chines[t], list_mathematics[t], list_English[t], total))
