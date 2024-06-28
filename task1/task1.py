def circular_array(array_length, length_interval):
    global j
    num_1 = []
    num_2 = []
    x = 0
    y = 0
    for i in range(1, array_length + 1):
        num_1.append(str(i))
    num_1 = num_1 * length_interval * 2
    while True:
        for j in num_1[:length_interval]:
            num_2.append(j)
            x += 1
            if x == length_interval:
                print(num_2[length_interval * y], end='')
                y += 1
                x = 0
                num_1 = num_1[length_interval - 1:]
        if j == '1':
            break


circular_array(int(input()), int(input()))
