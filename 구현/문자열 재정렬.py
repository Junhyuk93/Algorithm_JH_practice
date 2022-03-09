n = input()
n = list(n)

num_list = []
text_list = []

for i in range(len(n)):
    if str.isdigit(n[i]) == True:
        num_list.append(int(n[i]))
    else:
        text_list.append(n[i])

num_list = sum(num_list)

text_list.sort()

text = ''.join(text_list)
answer = text + str(num_list)
print(answer)