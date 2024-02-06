#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import area_calculator as calculator


if __name__ == '__main__':
    triangle_area = calculator.triangle.calculate_area(base=10, height=5)
    rectangle_area = calculator.rectangle.calculate_area(length=5, width=2)

    print('Triangle area: ', triangle_area)
    print('Rectangle area: ', rectangle_area)
