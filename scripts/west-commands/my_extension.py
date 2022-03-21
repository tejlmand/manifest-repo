import argparse
from pathlib import Path
from shutil import rmtree

from west.commands import WestCommand
from west import log

class MyCommand(WestCommand):

    def __init__(self):
        super().__init__(
            'my-command',
            '',
            '',
            accepts_unknown_args=False)

    def do_add_parser(self, parser_adder):
        parser = parser_adder.add_parser(
            self.name,
            help=self.help,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=self.description)
        return parser

    def do_run(self, args, unknown_args):
        print('Hello World')
