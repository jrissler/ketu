#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function
import glob
from multiprocessing import Pool

from ketu.photometry import process_file


def _wrap(fn):
    try:
        process_file(fn)
    except:
        print("failure: {0}".format(fn))
        import traceback
        traceback.print_exc()
        raise


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("tpfs",
                        help=("pattern for the TPF files. For example: "
                              "'data/c1/*/*/*.fits.gz'"))
    parser.add_argument("output_dir",
                        help="path where the LC files should be saved")
    parser.add_argument("-p", "--parallel", action="store_true",
                        help="should this be run in parallel?")

    args = parser.parse_args()

    filenames = glob.glob("data/c1/*/*/*.fits.gz")
    if args.parallel:
        pool = Pool()
        pool.map(_wrap, filenames)
    else:
        map(process_file, filenames)
