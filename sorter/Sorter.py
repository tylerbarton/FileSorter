"""
Organise music files in a directory into subdirectories based on parameters.
Usage:
  sorter <dir> -o <dir>
  sorter -h

Options:
    -d, --display-only      Display changes without doing actual actions

    -o, -output-dir <dir>   Change the destination of moved files.
    -v, --verbose           Display detailed information about the process
    -r, --revert            Revert previous file movements
    -h, --help              Display this help text.
"""

import os
import argparse


class Organizer(object):
    # cur_dir, target_dir, parent_dir, display_run, verbose

    def __init__(self):
        self.cur_dir = os.getcwd()  # os.listdir(self.path)
        self.home_dir = os.path.expanduser('~')

    def organize(self):
        print("Current Path:" + os.getcwd())
        print("Options:" + args.__str__())


def dir_path(string):
    """
    :param string: Path
    :return: true if the path is valid.
    """
    if os.path.isdir(string):
        return string
    else:
        raise argparse.ArgumentTypeError(f"is not a valid path" + string)


if __name__ == '__main__':
    # Commandline args
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', type=dir_path, help='targeted directory', metavar='path')
    parser.add_argument('-d', '--display-only', action='store_true', help='does not execute changes')
    parser.add_argument('-o',  default=os.getcwd(), type=dir_path,
                        help='output directory for the files', metavar='output_dir')
    parser.add_argument('-r', '--revert', help='restore files before last change was made',metavar='revert')
    parser.add_argument('-v', '--verbose', metavar='verbose')
    args = parser.parse_args()

    org = Organizer()
    org.organize()
