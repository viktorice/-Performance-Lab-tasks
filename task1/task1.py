def circular_array(array_length, length_interval):
    num = ''
    cum = ''
    x = 0
    y = 0
    for i in range(1, array_length + 1):
        num += str(i)
    num = num * length_interval * 2
    for k in range(length_interval * 2):
        for j in num[:length_interval]:
            cum += j
            x += 1
            if x == length_interval:
                print(cum[length_interval * y], end='')
                y += 1
                x = 0
                num = num[length_interval - 1:]
        if j == '1':
            break

circular_array(5, 4)
