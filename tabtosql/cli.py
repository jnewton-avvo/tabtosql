# -*- coding: utf-8 -*-

"""tabtosql.cli

This module contains the command line interface for `tabtosql`.


See the README for further details.

"""

import sys

import click

from tabtosql.workbook import convert


@click.command()
@click.argument('filename')
def main(filename):
    """Tableau Workbook SQL Extract Tool

    tabtosql is a command line tool for parsing sql queries & related
    information out of tableau workbooks (.twb & .twbx files). It works by
    taking a tableau workbook, parsing the xml, and formatting information
    about worksheets, connections to those worksheets, their connection(db)
    details, and the corresponding custom sql (assuming it exists) in a
    valid sql & human readable format.

        USAGE:

            $ tabtosql input.twb(x) > output.sql

    See the README for further details.
    """
    sys.stdout.write(convert(filename))


if __name__ == '__main__':
    main()