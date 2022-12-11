import csv
import datetime
import time
from typing import Any

import matplotlib.pyplot as plt

from config import filepath


class Plot:
    def __init__(self):
        self.csvpath = filepath
        self.orders_per_hours = [0 for _ in range(24)]
        self.orders_per_mouths = [0 for _ in range(12)]

    def csv_parser(self) -> list[tuple[Any, Any, Any, Any]]:
        csv_data = []
        with open(self.csvpath, newline='') as file:
            reader = csv.reader(file, delimiter=' ', quotechar='|')
            for n, row in enumerate(reader):
                if n == 0: continue
                date = row[0]
                time = row[1].split(';')[0]
                order_cord = row[1].split(';')[1:3]
                store_cord = row[1].split(';')[3:5]
                csv_data.append((date, time, order_cord, store_cord))
        return csv_data

    def order_per_hour(self, save: bool = False) -> None:
        for row in Plot().csv_parser():
            hour = int(row[1].split(':')[0])
            self.orders_per_hours[hour] += 1

        fig, ax = plt.subplots()

        ax.bar(list(map(str, range(24))), self.orders_per_hours, color="yellow", edgecolor="black")
        ax.grid(axis='y', linestyle='--')

        ax.set_ylabel('Кол-во заказов', fontsize=16, labelpad=15)
        ax.set_xlabel('Время', fontsize=16)
        ax.set_title('Распределение заказов по часам', fontsize=24)

        fig.set_figwidth(12)
        fig.set_figheight(6)
        if save:
            plt.savefig(f"{datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y_%H.%M.%S')}.png")
        plt.show()

    def order_per_mouth(self, save: bool = False) -> None:
        mouths = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                  "Ноябрь", "Декабрь"]
        for row in Plot().csv_parser():
            mouth = int(row[0].split('.')[1])
            self.orders_per_mouths[mouth - 1] += 1
        fig, ax = plt.subplots()
        ax.bar(mouths, self.orders_per_mouths, color="yellow", edgecolor="black")
        ax.grid(axis='y', linestyle='--')

        ax.set_ylabel('Кол-во заказов', fontsize=16, labelpad=15)
        ax.set_title('Распределение заказов по месяцам', fontsize=24)

        fig.set_figwidth(12)
        fig.set_figheight(6)
        if save:
            plt.savefig(f"{datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y_%H.%M.%S')}.png")
        plt.show()


def main():
    Plot().order_per_mouth()


if __name__ == '__main__':
    main()
