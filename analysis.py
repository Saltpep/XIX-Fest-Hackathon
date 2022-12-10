import csv

import matplotlib.pyplot as plt

from config import filepath

orders_in_times = [0 for _ in range(24)]


def csv_parser(path) -> None:
    global orders_in_times

    with open(path, newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        for n, row in enumerate(reader):
            if n > 0:
                # date = row[0]
                time = row[1].split(':')[0]
                orders_in_times[int(time)] += 1


def plot_bar() -> None:
    fig, ax = plt.subplots()

    ax.bar(list(map(str, range(24))), orders_in_times, color="yellow", edgecolor="black")
    ax.grid(axis='y', linestyle='--')

    ax.set_ylabel('Кол-во заказов', fontsize=16, labelpad=15)
    ax.set_xlabel('Время', fontsize=16)
    ax.set_title('Распределение заказов по часам', fontsize=24)

    fig.set_figwidth(12)
    fig.set_figheight(6)
    plt.savefig("plt.png")
    plt.show()


def main():
    csv_parser(path=filepath)
    plot_bar()


if __name__ == '__main__':
    main()
