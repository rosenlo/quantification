#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
Author: Rosen
Mail: rosenluov@gmail.com
File: grid.py
Created Time: Fri Mar 27 12:45:37 2020
"""

__version__ = '1.0.0'

from prettytable import PrettyTable
import math


def calc_buying_stocks(money, price):
    return money - int(math.ceil(money / price % 100)) / price


def grid(seq, price, money, step=0.05):
    in_position = 1.0
    median = 0.5
    t = PrettyTable(
        [seq, 'in_trigger', 'in_price', 'out_trigger', 'out_price', 'in_stock']
    )
    in_stock = money / price
    money_incr = 1

    while in_position > median:
        in_price = round(price * in_position, 3)
        in_trigger = round(in_price + 0.001, 3)

        out_position = round(in_position + step, 3)
        out_price = round(price * out_position, 3)
        out_trigger = round(out_price - 0.001, 3)

        t.add_row([
            in_position, in_trigger, in_price,
            out_trigger, out_price, in_stock
        ])

        money_incr += step
        in_position = round(in_position - step, 3)
        in_stock = calc_buying_stocks(money * money_incr, in_price)

    print(t)
