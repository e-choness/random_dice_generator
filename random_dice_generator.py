import random


def combination_to_dice(combination_index, num_dice, dice_sides):
    if combination_index == 0:
        return [1] * num_dice

    result = []
    while combination_index > 0:
        remainder = int(combination_index % dice_sides) + 1
        result.append(remainder)
        combination_index //= dice_sides

    if len(result) < num_dice:
        result += [1] * (num_dice - len(result))
    return result[::-1]


def dices_combination_generator(num_dice, dice_sides):
    num_combinations = pow(dice_sides, num_dice)
    random_index = random.randint(0, num_combinations)

    # result = []
    # for i in range(num_combinations):
    #     result.append(combination_to_dice(i,num_dice, dice_sides))

    return combination_to_dice(random_index, num_dice, dice_sides)


def main():
    input_flag = False
    while True:
        try:
            if not input_flag:
                print("How many dice do you have?")
                num_dice = int(input())
                print("How many sides are there on the dice?")
                dice_sides = int(input())
                input_flag = True
            print("You got: ", dices_combination_generator(num_dice, dice_sides))
            print("press any key to continue, or [e] to exit.")
            command = input()
            if command == "e":
                break
            else:
                print("Let's keep rolling dices!")
        except TypeError:
            print("Please enter numbers.")


if __name__ == "__main__":
    main()
