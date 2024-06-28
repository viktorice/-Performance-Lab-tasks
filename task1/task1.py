def circular_array(array_length, length_interval):
    num_1 = ''
    num_2 = ''
    x = 0
    y = 0
    for i in range(1, array_length + 1):
        num_1 += str(i)
    num_1 = num_1 * length_interval * 2
    for k in range(length_interval * 2):
        for j in num_1[:length_interval]:
            num_2 += j
            x += 1
            if x == length_interval:
                print(num_2[length_interval * y], end='')
                y += 1
                x = 0
                num_1 = num_1[length_interval - 1:]
        if j == '1':
            break

circular_array(int(input()), int(input()))
