n = list(input())

first_num = n[0]
save_list = []
for i in range(1,len(n)):
    save_list.append(int(first_num) + int(n[i]))
    save_list.append(int(first_num) * int(n[i]))
    save_list.sort()
    first_num = save_list[-1]
print(save_list[-1])