# Задача 34
data = list(map(str,input().split()))

# print(data[1])
flag = 1
count_gl = []
for c in range(len(data)):
    count_gl.append(len(list(filter(lambda x: x =='а', data[c]))))

print(count_gl)
for c in range(len(data)):
    if count_gl[0] != count_gl[c]:
        flag = 0
if flag == 0:
    print('Пам парам')
else:
    print ('Парам пам-пам')

# Задача 36
def operation(x,y):
    return x*y
def print_table_operation(operation, num_colums = 6, num_rows = 6):
    for y in range(1, num_rows+1):
        nums = []
        for x in range(1, num_colums+1):
            num = operation(x, y)
            nums.append(num)
        print(nums)

print_table_operation(operation, num_colums = 6, num_rows = 6)
