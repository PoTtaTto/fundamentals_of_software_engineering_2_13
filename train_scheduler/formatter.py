# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# Standard
import sys


def show_help():
    """
    Выводит список доступных команд на экран.

    """
    print("Список команд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поездов;")
    print("select <пункт назначения> - запросить поезда с пунктом назначения;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def show_error(command: str):
    """
    Выводит ошибку о недопустимой команде на экран.

    """
    print(f'Неизвестная команда {command}', file=sys.stderr)
