from data import data
import random


def random_select():
    first_select_random = random.choice(data)
    second_select_random = random.choice(data)
    if second_select_random == first_select_random:
        second_select_random = random.choice(data)
    return first_select_random, second_select_random


def compare_random():
    if random_select()[0]["follower_count"] > random_select()[1]["follower_count"]:
        return 0
    else:
        return 1


def play_game():

    is_game_over = False
    score = 0

    while not is_game_over:
        print("Who has the highest follower count?")
        print(f'Does {random_select()[0]["name"]} have a higher follower count then {random_select()[1]["name"]} or lower?\n[higher or lower?]')
        print(f'score = {score}')
        choose = input(": ").lower()
        if choose == "higher":
            choice = 0
        else:
            choice = 1
        answer = compare_random()
        if choice == answer:
            print("you win")
            score += 1
        else:
            print("you lose")
            is_game_over = True


play_game()