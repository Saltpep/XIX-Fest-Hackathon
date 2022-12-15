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
        self.orders_per_day = [0 for _ in range(31)]
        self.orders_per_week = [0 for _ in range(7)]
        self.average_orders_per_week = [0 for _ in range(7)]

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


    def order_per_day(self, save: bool = False):
        for row in Plot().csv_parser():
            day = int(row[0].split('.')[0])
            self.orders_per_day[day-1] += 1
        fig, ax = plt.subplots()
        ax.bar(list(map(str, range(1, 32))), self.orders_per_day, color="yellow", edgecolor="black")
        ax.grid(axis='y', linestyle='--')

        ax.set_ylabel('Кол-во заказов', fontsize=16, labelpad=15)
        ax.set_title('Распределение заказов по дням', fontsize=24)

        fig.set_figwidth(12)
        fig.set_figheight(6)
        if save:
            plt.savefig(f"{datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y_%H.%M.%S')}.png")
        plt.show()

    def order_per_week(self, save: bool = False):
        weeks = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

        for row in Plot().csv_parser():
            date = row[0].split('.')
            week = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
            self.orders_per_week[week.weekday()] += 1

        fig, ax = plt.subplots()
        ax.bar(weeks, self.orders_per_week, color="yellow", edgecolor="black")
        ax.grid(axis='y', linestyle='--')

        ax.set_ylabel('Кол-во заказов', fontsize=16, labelpad=15)
        ax.set_title('Распределение заказов в неделе', fontsize=24)

        fig.set_figwidth(12)
        fig.set_figheight(6)
        if save:
            plt.savefig(f"{datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y_%H.%M.%S')}.png")
        plt.show()

    def average_order_per_week(self, save: bool = False):
        weeks = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс", ]
        days = 0
        temp_dw = []
        for row in Plot().csv_parser():
            date = row[0].split('.')
            day_week = list(map(int, date[:2]))
            if day_week not in temp_dw:
                days += 1
                temp_dw.append(day_week)
            week = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
            self.average_orders_per_week[week.weekday()] += 1
        for i in range(len(self.orders_per_week)):
            self.average_orders_per_week[i] /= days

        average_order_per_day_in_week = sum(self.average_orders_per_week) / len(self.average_orders_per_week)
        print(f"Среднее кол-во заказов в день: {round(average_order_per_day_in_week)}")

        fig, ax = plt.subplots()
        ax.bar(weeks, self.average_orders_per_week, color="yellow", edgecolor="black")
        ax.grid(axis='y', linestyle='--')

        ax.set_ylabel('Кол-во заказов', fontsize=16, labelpad=15)
        ax.set_title('Среднее кол-во заказов по дням в неделе', fontsize=24)

        fig.set_figwidth(12)
        fig.set_figheight(6)
        if save:
            plt.savefig(f"{datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y_%H.%M.%S')}.png")
        plt.show()


def main():
    Plot().order_per_hour()
    Plot().order_per_mouth()
    Plot().order_per_day()
    Plot().order_per_week()
    Plot().average_order_per_week()


if __name__ == '__main__':
    main()
