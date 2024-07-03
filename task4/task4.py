import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file', type=str)

args = parser.parse_args()


def minimum_number_of_moves(txt):
    with open(txt) as file:
        array = [row.strip() for row in file]
    array = [int(num) for num in array]
    number_of_moves = []
    for i in range(len(array)):
        amount = 0
        nums = [array[i]]
        nums *= len(array)
        for k in range(len(array)):
            amount += abs(nums[i] - array[k])
        number_of_moves.append(amount)
    print(min(number_of_moves))


minimum_number_of_moves(args.file)