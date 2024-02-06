#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Project
import train_scheduler as scheduler


def start_program():
    trains = []
    while True:
        cmd = input('>>> ')
        cmd_parts = cmd.split(maxsplit=1)
        match cmd_parts[0]:
            case 'add':
                scheduler.manipulator.add_train(trains)
            case 'list':
                scheduler.manipulator.list_trains(trains)
            case 'select':
                scheduler.manipulator.select_train(trains, cmd_parts)
            case 'help':
                scheduler.formatter.show_help()
            case 'exit':
                break
            case _:
                scheduler.formatter.show_error(command=cmd)


if __name__ == '__main__':
    start_program()
