from math import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file1', type=str)
parser.add_argument('file2', type=str)

args = parser.parse_args()


def point_position(txt_1, txt_2):
    with open(txt_1) as file_1:
        array_1 = [row.split() for row in file_1]
    center_circle = [int(num) for num in array_1[0]]
    radius = int(''.join(array_1[1]))
    with open(txt_2) as file_2:
        array_2 = [row.split() for row in file_2]
    for i in array_2:
        pyth_theorem = sqrt((int(i[0]) - center_circle[0]) ** 2 + (int(i[1]) - center_circle[1]) ** 2)
        if pyth_theorem < radius:
            print(1)
        elif pyth_theorem == radius:
            print(0)
        else:
            print(2)


point_position(args.file1, args.file2)
