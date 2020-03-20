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
import sys
import os
import argparse
import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
import shutil

class InvalidFileException(Exception):
    """Special file located"""
    pass

class Organizer(object):
    # cur_dir, target_dir, parent_dir, display_run, verbose

    def __init__(self):
        if args.src_dir is None:
            args.src_dir = os.getcwd()
        if args.dst_dir is None:
            args.dst_dir = os.getcwd()

    def organize(self):
        """
        Organize the files into
        :return: True if successful
        """
        if args.verbose:
            print("Options:" + args.__str__())

        # Try to do singles

        file_list = os.listdir(args.src_dir)
        dir_length = len(file_list)
        for filename in file_list:
            file_path = args.src_dir + "\\" + filename
            # Goal: %artist%/Singles|Albums/File
            if os.path.isdir(file_path):
                # TODO: keep directory name
                print("dir: " + file_path)
                # TODO: count the amount of files in here: 1, 2 or same name => single

            elif os.path.isfile(file_path):
                #print("file: " + file_path)
                audio = mutagen.File(file_path)

                # print(audio['artist'])

                if str.endswith(file_path, ".mp3"):
                    # MP3
                    audio = EasyID3(file_path)
                    print(audio.valid_keys.keys())

                    # album, artist, albumartist, tracknumber

                if str.endswith(file_path, ".flac"):
                    # FLAC
                    audio = FLAC(file_path)
                    print(audio["title"])

            else:
                raise InvalidFileException("Invalid file found: " + file_path)

    def make_directories(self):
        """
        Makes directory if it does not exist.
        :return: True if successful
        """



def dir_path(string):
    """
    :param string: Directory
    :return: true if the directory is valid.
    """
    if os.path.isdir(string):
        return string
    else:
        raise argparse.ArgumentTypeError(f"is not a valid path" + string)


if __name__ == '__main__':
    # Commandline args
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', '-src', '--src_dir', type=dir_path, help='source directory', metavar='src_dir')
    parser.add_argument('-d', '--display-only', action='store_true', help='does not execute changes')
    parser.add_argument('-o', '--dst_dir',  default=os.getcwd(), type=dir_path,
                        help='destination directory for the files', metavar='dst_dir')
    parser.add_argument('-r', '--revert', help='restore files before last change was made',metavar='revert')
    parser.add_argument('-v', '--verbose', metavar='verbose')
    args = parser.parse_args()

    org = Organizer()
    org.organize()
