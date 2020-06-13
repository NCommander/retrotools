#!/usr/bin/python3

# SLS Image Creator
# Author: Michael Casadevall <michael@casadevall.pro> 2020
#
# This script is in the public domain

import os
import subprocess
import time

disk_src_dir = './SLS/'
disk_list = [
    'a2',
    'a3',
    'a4',
    'b1',
    'b2',
    'b3',
    'b4',
    'b5',
    'b6',
    'b7',
    'b8',
    'c1',
    'c2',
    'c3',
    'd1',
    'd2',
    's1',
    't1',
    't2',
    't3',
    'x1',
    'x2',
    'x3',
    'x4',
    'x5',
    'x6',
    'x7',
    'x8',
    'x9',
    'x10'
]

def create_disk(disk_name):
    img_name = disk_name + ".img"
    # Create a blank disk image
    print("Creating " + disk_name)
    with open(img_name, "w") as f:
            f.seek(1474560-1)
            f.write("\0")

    # Now format it
    subprocess.run(["mkfs.msdos", img_name])


def copy_files(src_dir, disk_name):
    img_name = disk_name + ".img"
    for filename in os.listdir(src_dir + disk_name):
        subprocess.run(["mcopy", "-vi", img_name, src_dir + disk_name + "/" + filename, "::"])

def main():
    for disk_name in disk_list:
        create_disk(disk_name)
        copy_files(disk_src_dir, disk_name)
        print()
        time.sleep(0.2)
    print("== SLS MEDIA RECREATED! ==")
    return

if __name__ == '__main__':
    main()

