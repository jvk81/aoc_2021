with open('/Users/juha.kuusela/koodailua/harjoittelua/AOC_2021/day_1_inputs.txt', 'r') as f:
    data = f.read()


data_list = data.split('\n')

for i in range(0, len(data_list)):
    data_list[i] = int(data_list[i])

One_star = 0

Two_star = 0

for i in range(len(data_list)):
    if data_list[i] >= 1 and data_list[i] > data_list[i-1]:
        One_star += 1   

for i in range(len(data_list)):
    if data_list[i] >= 3 and data_list[i] + data_list[i-1] + data_list[i-2] > data_list[i-3] + data_list[i-2] + data_list[i-1]:
        Two_star += 1
print(data_list)

print(One_star)
print(Two_star)
