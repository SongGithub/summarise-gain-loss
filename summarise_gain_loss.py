#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
import sys


def handle_stdin():
    return sys.stdin.readlines()


def calculate_diff(previous_data, current_data):
    return round((Decimal(current_data) - Decimal(previous_data)), 2)


def summarise_prices(input_array):
    gain = 0
    loss = 0

    for i in range(1, len(input_array)):
        diff = calculate_diff(input_array[i-1], input_array[i])
        if diff >=0:
            gain += diff
        else:
            loss += diff

    return {
            "GAIN": str(gain),
            "LOSS": str(loss)
            }


def output(result_dict):
    print(result_dict["GAIN"])
    print(result_dict["LOSS"])


if __name__ == '__main__':
    stdin_data = handle_stdin()
    summary = summarise_prices(stdin_data)
    output(summary)
