"""
python3 程序开发指南的练习
"""

import os


def main():
    child = os.path.join(os.path.dirname(__file__),
                         "grepword-p-child.py")

    opts, word, args = parse_options()
    filelist = get_files(args, opts.recurse)
    files_per_process = len(filelist) // opts.count
    start, end = 0, files_per_process + (len(filelist) % opts.count)
    number = 1
    