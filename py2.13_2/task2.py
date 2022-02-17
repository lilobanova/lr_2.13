#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from humans import print
from humans import data_commands as d_c

if __name__ == '__main__':
    humans = []
    while True:
        command = print.get_command()
        if command == 'exit':
            break

        elif command == 'add':
            humans.append(d_c.add())
            if len(humans) > 1:
                humans.sort(key=lambda item: item.get('name'))

        elif command == 'list':
            print.print_list(humans)

        elif command.startswith('select'):
            d_c.select(command, humans)

        elif command == 'help':
            print.print_help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
