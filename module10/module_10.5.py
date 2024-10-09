import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':
    # Линейный вызов
    start = datetime.now()
    for i in range(1, 5):
        read_info(f'./files/file {i}.txt')
    end = datetime.now()
    print(f'{end - start} линейный')

    # Многопроцессный вызов
    all_name = [f'./files/file {i}.txt' for i in range(1, 5)]
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, all_name)
        end = datetime.now()
        print(f'{end - start} многопроцессный')