import csv


def csv_reader(url, data):
    csv_file = csv.reader(open(url, encoding='GBK'))

    for item in csv_file:
        data.append(item)


def min_max_nor(x, Max, Min):
    x = (x - Min) / (Max - Min)
    return x


def norm_list(list):
    Max = max(list)
    Min = min(list)
    new_list = []
    for item in list:
        new_item = min_max_nor(item, Max, Min)
        new_list.append(new_item)
    return new_list


data = []
csv_reader('data_2.csv', data)
ids = data[0]
p = norm_list(list(map(int, data[1])))
ac = norm_list(list(map(int, data[2])))
pr = norm_list(list(map(float, data[3])))

dic = {}

for index in range(0, 99):
    value = p[index] * 0.3 + ac[index] * 0.3 + pr[index] * 0.4
    # value = p[index] * 0.5 + ac[index] * 0.5
    dic.update({ids[index]: value})

dicSortList = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for item in dicSortList:
    print(item)
