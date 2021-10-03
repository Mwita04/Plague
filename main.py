import os
from random import randint


def get_days():
    day = randint(1, 5)
    return day


def make_commit(days: int):
    if days < 1:
        # Push
        return os.system('git push')
    else:
        dates = f'{days} days ago'

        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')

        # Staging
        os.system('git add data.txt')

        # commit
        os.system('git commit --date="'+dates+'" -m "First Commit"')

        d = get_days()
        return days * make_commit(days-d)


make_commit(75)
